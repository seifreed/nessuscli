"""Filesystem adapter for persisted API responses."""

from __future__ import annotations

import json
from pathlib import Path

from .types import ResponseValue


class FileOutputWriter:
    """Write response values to local files."""

    def write(self, destination: str | Path, data: ResponseValue) -> str:
        """Write bytes, text, or JSON data to the requested path."""
        path = Path(destination)
        path.write_bytes(_output_bytes(data))
        return str(path)


def _output_bytes(data: ResponseValue) -> bytes:
    if isinstance(data, bytes):
        return data
    if isinstance(data, str):
        return data.encode()
    return json.dumps(data).encode()
