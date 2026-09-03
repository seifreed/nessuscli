"""Pure request planning and payload encoding helpers."""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import quote, urlencode

from .contract import Operation
from .errors import NessusError
from .types import JsonValue


@dataclass(frozen=True, slots=True)
class GroupedArguments:
    """Arguments grouped according to an operation's request contract."""

    path: dict[str, JsonValue]
    query: dict[str, JsonValue]
    payload: dict[str, JsonValue]


def group_arguments(
    operation: Operation,
    arguments: dict[str, JsonValue],
    path: dict[str, JsonValue] | None,
    query: dict[str, JsonValue] | None,
    payload: dict[str, JsonValue] | None,
) -> GroupedArguments:
    """Route named arguments and validate required request parameters."""
    parameters = operation.definition.get("request", {}).get("parameters", {})
    path_values = dict(path or {})
    query_values = dict(query or {})
    payload_values = dict(payload or {})
    uri_path_names = set(re.findall(r"{([^{}]+)}", operation.uri))
    path_names = set(parameters.get("path", {})) | uri_path_names
    query_names = set(parameters.get("query", {}))
    payload_names = set(parameters.get("payload", {}))
    for values in (query_values, payload_values):
        for name in tuple(values):
            if name in uri_path_names:
                path_values[name] = values.pop(name)
    for name, value in arguments.items():
        if name in path_names:
            path_values[name] = value
        elif name in query_names:
            query_values[name] = value
        elif name in payload_names or operation.method not in {"GET", "DOWNLOAD"}:
            payload_values[name] = value
        else:
            query_values[name] = value
    for values in (path_values, query_values, payload_values):
        for name in tuple(values):
            if values[name] is None:
                del values[name]
    missing: list[str] = []
    for category in ("path", "query", "payload"):
        for name, definition in parameters.get(category, {}).items():
            values = (
                path_values
                if category == "path" or name in uri_path_names
                else query_values if category == "query" else payload_values
            )
            if definition.get("required") and (
                name not in values or values[name] is None
            ):
                missing.append(name)
    for name in uri_path_names:
        if (
            name not in path_values or path_values[name] is None
        ) and name not in missing:
            missing.append(name)
    if missing:
        raise NessusError(f"Missing required parameters: {', '.join(missing)}")
    return GroupedArguments(path_values, query_values, payload_values)


def build_url(
    base_url: str, uri: str, path: dict[str, JsonValue], query: dict[str, JsonValue]
) -> str:
    """Render URI placeholders and query values into an encoded URL."""
    segments = []
    for segment in uri.split("/"):
        if segment.startswith("{") and segment.endswith("}"):
            name = segment[1:-1]
            if name not in path:
                raise NessusError(f"Missing path parameter: {name}")
            segments.append(quote(str(path[name]), safe=""))
        else:
            segments.append(segment)
    url = f"{base_url}/{'/'.join(segments)}"
    return f"{url}?{urlencode(query, doseq=True)}" if query else url
