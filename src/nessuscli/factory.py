"""Composition roots for ready-to-use Nessus clients."""

from __future__ import annotations

from .client import NessusClient
from .config import Settings
from .file_output import FileOutputWriter
from .generated import TypedNessusClient
from .transport import UrllibTransport


def create_client(settings: Settings) -> NessusClient:
    """Create a client backed by the standard urllib transport."""
    return NessusClient(settings, UrllibTransport(settings), FileOutputWriter())


def create_typed_client(settings: Settings) -> TypedNessusClient:
    """Create a typed client backed by the standard urllib transport."""
    return TypedNessusClient(settings, UrllibTransport(settings), FileOutputWriter())
