from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from pytest import CaptureFixture

from nessuscli.cli import _json_object, _parse_arguments, _print_result, main
from nessuscli.contract import load_contract


def test_cli_resources(capsys: CaptureFixture[str]) -> None:
    assert main(["resources"]) == 0
    output = capsys.readouterr().out
    resources = json.loads(output)
    assert "scans" in resources
    assert "details" in resources["scans"]


def test_cli_rejects_invalid_arguments(capsys: CaptureFixture[str]) -> None:
    assert main(["call", "scans", "details", "--path", "[]"]) == 1
    assert "must contain a JSON object" in capsys.readouterr().err
    assert main(["call", "scans", "details", "--arg", "invalid"]) == 1
    assert "expected NAME=VALUE" in capsys.readouterr().err


def test_cli_argument_parser() -> None:
    assert _parse_arguments(["one=1", "two=true", "three=text"]) == {
        "one": 1,
        "two": True,
        "three": "text",
    }
    assert _json_object("{}", "path") == {}
    with pytest.raises(ValueError, match="cannot be empty"):
        _parse_arguments(["=value"])


def test_cli_call_and_print_result(
    api_server: str, capsys: CaptureFixture[str]
) -> None:
    assert main(["--base-url", api_server, "scans", "details", "--scan-id", "7"]) == 0
    assert '"path": "/scans/7"' in capsys.readouterr().out
    assert (
        main(
            ["--base-url", api_server, "terrascan", "delete-config", "--config-id", "7"]
        )
        == 0
    )
    assert '"path": "/tools/terrascan/configs/7"' in capsys.readouterr().out
    assert (
        main(
            ["--base-url", api_server, "call", "scans", "details", "--arg", "scan_id=7"]
        )
        == 0
    )
    assert '"path": "/scans/7"' in capsys.readouterr().out
    _print_result(b"bytes")
    _print_result("text")
    _print_result({"value": 1})
    captured = capsys.readouterr()
    assert captured.out.startswith("bytestext")
    assert '"value": 1' in captured.out


def test_cli_can_call_every_catalog_operation(
    api_server: str, tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    operation_count = 0
    for resource, definition in load_contract()["resources"].items():
        for name, operation in definition["methods"].items():
            arguments = _required_arguments(operation)
            command = ["--base-url", api_server, resource, name]
            command.extend(
                argument
                for value in arguments
                for argument in ("--arg", f"{value[0]}={json.dumps(value[1])}")
            )
            if (
                operation.get("request", {})
                .get("parameters", {})
                .get("body", {})
                .get("Request Body", {})
                .get("required")
            ):
                command.extend(("--body", "{}"))
            if resource == "file" or name.endswith("upload"):
                upload = tmp_path / "upload.bin"
                upload.write_bytes(b"upload")
                command.extend(("--file", str(upload)))
            if operation["method"] == "DOWNLOAD":
                command.extend(("--output", str(tmp_path / f"{resource}-{name}.out")))
            assert main(command) == 0
            capsys.readouterr()
            operation_count += 1
    assert operation_count == 166


def _required_arguments(operation: dict[str, object]) -> list[tuple[str, object]]:
    request = operation.get("request", {})
    if not isinstance(request, dict):
        return []
    parameters = request.get("parameters", {})
    if not isinstance(parameters, dict):
        return []
    arguments: dict[str, object] = {}
    for category in ("path", "query", "payload"):
        values = parameters.get(category, {})
        if not isinstance(values, dict):
            continue
        for name, definition in values.items():
            if isinstance(definition, dict) and definition.get("required"):
                arguments[name] = _sample_value(definition.get("type"))
    for name in re.findall(r"{([^{}]+)}", str(operation.get("uri", ""))):
        arguments.setdefault(name, 1)
    return list(arguments.items())


def _sample_value(parameter_type: object) -> object:
    if parameter_type in {"array", "list"}:
        return [1]
    if parameter_type in {"boolean", "bool"}:
        return True
    if parameter_type in {"integer", "int", "number"}:
        return 1
    if parameter_type in {"object", "json"}:
        return {}
    return "value"
