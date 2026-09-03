"""Application ports used by nessuscli."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from .types import ResponseValue


class Transport(Protocol):
    """Boundary used by the client to send an already-built request."""

    def request(
        self, method: str, url: str, body: bytes | None, content_type: str | None
    ) -> ResponseValue:
        """Send a request and decode its response."""


class OutputWriter(Protocol):
    """Boundary used to persist a response outside the application layer."""

    def write(self, destination: str | Path, data: ResponseValue) -> str:
        """Persist a response and return its destination."""
