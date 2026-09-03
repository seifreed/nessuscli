"""Response decoding policies."""

from __future__ import annotations

import json

from .types import ResponseValue


def decode_response(raw: bytes, content_type: str) -> ResponseValue:
    """Decode JSON responses and preserve text responses losslessly."""
    if not raw:
        return None
    if "json" in content_type.lower():
        try:
            return json.loads(raw)
        except json.JSONDecodeError, UnicodeDecodeError:
            pass
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw
