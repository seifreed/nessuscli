"""Request body encoders."""

from __future__ import annotations

import json
import mimetypes
import re
import uuid
from pathlib import Path

from .contract import Operation
from .errors import NessusError
from .types import JsonValue


def json_body(
    operation: Operation,
    payload: dict[str, JsonValue],
    body: JsonValue | None,
) -> tuple[bytes | None, str | None]:
    """Encode a JSON request body when the operation needs one."""
    if (
        operation.method in {"GET", "DELETE", "DOWNLOAD"}
        and body is None
        and not payload
    ):
        return None, None
    value = body if body is not None else payload
    return json.dumps(value).encode(), "application/json"


def multipart(
    file_path: str | Path, payload: dict[str, JsonValue]
) -> tuple[bytes, str]:
    """Encode a file and additional fields as multipart form data."""
    path = Path(file_path)
    if not path.is_file():
        raise NessusError(f"File does not exist: {path}")
    boundary = f"nessuscli-{uuid.uuid4().hex}"
    filename = re.sub(r'["\r\n]', "", path.name) or "upload"
    content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    chunks = [
        (
            f'--{boundary}\r\nContent-Disposition: form-data; name="Filedata"; '
            f'filename="{filename}"\r\nContent-Type: {content_type}\r\n\r\n'
        ).encode(),
        path.read_bytes(),
        b"\r\n",
    ]
    for name, value in payload.items():
        field_name = re.sub(r'["\r\n]', "", name) or "field"
        chunks.append(
            (
                f'--{boundary}\r\nContent-Disposition: form-data; name="{field_name}"'
                f"\r\n\r\n{value}\r\n"
            ).encode()
        )
    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"
