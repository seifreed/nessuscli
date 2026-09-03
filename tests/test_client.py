from __future__ import annotations

import inspect
import json
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import pytest

from nessuscli import NessusClient, Settings, create_typed_client
from nessuscli.encoding import _sanitize_header_value, json_body, multipart
from nessuscli.errors import ApiError, NessusError
from nessuscli.file_output import FileOutputWriter
from nessuscli.request import build_url
from nessuscli.response import decode_response
from nessuscli.transport import UrllibTransport, _ssl_context
from nessuscli.types import JsonValue, ResponseValue


class ApiHandler(BaseHTTPRequestHandler):
    requests: list[tuple[str, str, dict[str, str], bytes]] = []

    def _handle(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        headers = {key: value for key, value in self.headers.items()}
        self.requests.append((self.command, self.path, headers, body))
        if self.path == "/error":
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"message":"bad request"}')
            return
        if self.path.endswith("/download"):
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.end_headers()
            self.wfile.write(b"report-bytes")
            return
        if self.path == "/text" or self.path.endswith("?text=1"):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"plain text")
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(
            json.dumps({"method": self.command, "path": self.path}).encode()
        )

    def do_DELETE(self) -> None:
        self._handle()

    def do_GET(self) -> None:
        self._handle()

    def do_POST(self) -> None:
        self._handle()

    def do_PUT(self) -> None:
        self._handle()

    def log_message(self, format: str, *args: Any) -> None:
        return


@pytest.fixture()
def api_server() -> Iterator[str]:
    ApiHandler.requests = []
    server = ThreadingHTTPServer(("127.0.0.1", 0), ApiHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()
        server.server_close()


def client_for(base_url: str) -> NessusClient:
    settings = Settings(
        base_url=base_url,
        access_key="access",
        secret_key="secret",
        token="token",
    )
    return NessusClient(
        settings,
        UrllibTransport(settings),
        FileOutputWriter(),
    )


def test_contract_and_dynamic_resource_access(api_server: str) -> None:
    client = client_for(api_server)
    assert len(client.resources) == 25
    assert len(client.operation_list) == 166
    assert "details" in client.operations_for("scans")
    result = _mapping(client.scans.details(scan_id=7))
    assert result["path"] == "/scans/7"
    assert _mapping(client.scans.details(scan_id="a/b"))["path"] == "/scans/a%2Fb"
    with pytest.raises(AttributeError, match="Unknown Nessus resource"):
        client.unknown
    with pytest.raises(AttributeError, match="Unknown Nessus operation"):
        client.scans.unknown
    with pytest.raises(NessusError, match="Unknown Nessus operation"):
        client.call("scans", "unknown")


def test_query_payload_body_auth_and_output(api_server: str, tmp_path: Path) -> None:
    client = client_for(api_server)
    listed = client.scans.list(folder_id=3, query_value=["one", "two"])
    assert _mapping(listed)["method"] == "GET"
    post = client.scans.create(
        body={"custom": True},
        uuid="template",
        settings={"name": "scan"},
    )
    assert _mapping(post)["method"] == "POST"
    request = ApiHandler.requests[-1]
    headers = {key.lower(): value for key, value in request[2].items()}
    assert headers["x-apikeys"] == "accessKey=access; secretKey=secret;"
    assert headers["x-cookie"] == "token=token;"
    assert json.loads(request[3]) == {"custom": True}

    filtered = client.agents.list(limit=2)
    assert _mapping(filtered)["method"] == "GET"
    assert ApiHandler.requests[-1][1] == "/agents?limit=2"
    client.call("agents", "list", query={"limit": None})
    assert ApiHandler.requests[-1][1] == "/agents"
    client.call("agents", "list", limit=None)
    assert ApiHandler.requests[-1][1] == "/agents"

    destination = tmp_path / "report.bin"
    result = client.call(
        "scans", "export-download", scan_id=1, file_id=2, output_path=destination
    )
    assert result == str(destination)
    assert destination.read_bytes() == b"report-bytes"
    text_destination = tmp_path / "response.txt"
    client.call("agents", "list", query={"text": 1}, output_path=text_destination)
    assert text_destination.read_bytes() == b"plain text"
    json_destination = tmp_path / "response.json"
    client.call("agents", "list", output_path=json_destination)
    assert json.loads(json_destination.read_bytes()) == {
        "method": "GET",
        "path": "/agents",
    }


def test_upload_and_error_handling(api_server: str, tmp_path: Path) -> None:
    upload = tmp_path / "policy.nessus"
    upload.write_bytes(b"policy")
    assert (
        _sanitize_header_value('policy"\r\nX-Injected: value.nessus', "upload")
        == "policyX-Injected: value.nessus"
    )
    client = client_for(api_server)
    result = client.file.upload(file_path=upload, no_enc=1)
    assert _mapping(result)["method"] == "POST"
    body = ApiHandler.requests[-1][3]
    assert b'filename="policy.nessus"' in body
    assert b"\r\nX-Injected" not in body
    assert b'name="no_enc"' in body
    client.file.upload(
        file_path=upload,
        payload={'field"\r\nX-Injected: value': 1},
    )
    body = ApiHandler.requests[-1][3]
    assert b'name="fieldX-Injected: value"' in body
    assert b'field"\r\nX-Injected' not in body
    with pytest.raises(ApiError, match="HTTP 400") as caught:
        client._transport.request("GET", f"{api_server}/error", None, None)
    assert caught.value.status_code == 400
    with pytest.raises(NessusError, match="File does not exist"):
        client.file.upload(file_path=tmp_path / "missing")


def test_validation_and_helpers(api_server: str) -> None:
    client = client_for(api_server)
    with pytest.raises(NessusError, match="Missing required parameters"):
        client.scans.details()
    with pytest.raises(NessusError, match="Missing required parameters"):
        client.scans.details(scan_id=None)
    assert build_url("http://example.test", "x/{id}", {"id": 1}, {"a": [1, 2]}) == (
        "http://example.test/x/1?a=1&a=2"
    )
    assert decode_response(b"plain", "text/plain") == "plain"
    assert decode_response(b"{bad", "application/json") == "{bad"
    assert decode_response(b"\xff", "text/plain") == b"\xff"
    assert decode_response(b"\xff", "application/json") == b"\xff"
    assert decode_response(b"", "application/json") is None
    with pytest.raises(NessusError, match="Missing path parameter"):
        build_url("http://example.test", "x/{id}", {}, {})
    with pytest.raises(NessusError, match="request_body"):
        client.permissions.change(object_type="scan", object_id=1)
    with pytest.raises(NessusError, match="file_path"):
        client.call("file", "upload")
    client.call("profiles", "add-profile-members", query={"profile_uuid": "value"})
    with pytest.raises(NessusError, match="config_id"):
        client.call("terrascan", "delete-config")
    assert _ssl_context(Settings(verify_ssl=False)) is not None
    get_operation = next(
        operation for operation in client.operation_list if operation.method == "GET"
    )
    assert json_body(get_operation, {}, None) == (None, None)
    with TemporaryDirectory() as directory:
        path = Path(directory) / "file.bin"
        path.write_bytes(b"data")
        body, content_type = multipart(path, {"value": 1})
        assert b"data" in body
        assert content_type.startswith("multipart/form-data; boundary=")


def test_connection_error() -> None:
    settings = Settings(base_url="http://127.0.0.1:1")
    client = NessusClient(settings, UrllibTransport(settings), FileOutputWriter())
    with pytest.raises(NessusError, match="Unable to reach Nessus"):
        client.server.status()


def test_generated_typed_wrappers_cover_every_operation(
    api_server: str, tmp_path: Path
) -> None:
    client = create_typed_client(
        Settings(base_url=api_server, access_key="access", secret_key="secret")
    )
    assert client.config.base_url == api_server
    assert _mapping(client.settings.list_advanced())["method"] == "GET"
    for operation in client.operation_list:
        resource = getattr(client, operation.resource.replace("-", "_"))
        method_name = operation.name.replace("-", "_")
        if method_name == "import":
            method_name = "import_"
        method = getattr(resource, method_name)
        arguments = {
            name: _typed_sample(name, parameter.annotation, tmp_path)
            for name, parameter in inspect.signature(method).parameters.items()
        }
        result = method(**arguments)
        if operation.method == "DOWNLOAD":
            assert Path(result).exists()


def _typed_sample(name: str, annotation: object, tmp_path: Path) -> object:
    if name == "file_path":
        path = tmp_path / "upload.bin"
        path.write_bytes(b"upload")
        return path
    if name == "output_path":
        return tmp_path / "download.bin"
    annotation_name = str(annotation)
    if name == "request_body" or "dict" in annotation_name:
        return {}
    if "list" in annotation_name:
        return [1]
    if "bool" in annotation_name:
        return True
    if "int" in annotation_name or "float" in annotation_name:
        return 1
    return "value"


def _mapping(value: ResponseValue) -> dict[str, JsonValue]:
    if not isinstance(value, dict):
        raise AssertionError(f"Expected an object response, got {type(value).__name__}")
    return value
