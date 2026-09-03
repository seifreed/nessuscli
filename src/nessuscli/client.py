"""Nessus HTTP client with contract-driven access to every documented operation."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from .config import Settings
from .contract import Operation, index_operations, load_contract
from .encoding import json_body, multipart
from .errors import NessusError
from .ports import OutputWriter, Transport
from .request import build_url, group_arguments
from .types import JsonValue, ResponseValue


class Resource:
    """Dynamic proxy exposing operations for one API resource."""

    def __init__(self, client: NessusClient, resource: str) -> None:
        self._client = client
        self._resource = resource

    def __getattr__(self, operation: str) -> Callable[..., ResponseValue]:
        name = operation.replace("_", "-")
        if name not in self._client.operations_for(self._resource):
            raise AttributeError(
                f"Unknown Nessus operation: {self._resource}.{operation}"
            )
        return lambda **arguments: self._client.call(self._resource, name, **arguments)


class NessusClient:
    """Client for all operations described by the Nessus API JSON contract."""

    def __init__(
        self, settings: Settings, transport: Transport, output_writer: OutputWriter
    ) -> None:
        self.config = settings
        self._contract = load_contract()
        self._operations = index_operations(self._contract)
        self._transport = transport
        self._output_writer = output_writer

    @property
    def resources(self) -> tuple[str, ...]:
        """Return all resource names in the API contract."""
        return tuple(self._contract["resources"])

    @property
    def operation_list(self) -> tuple[Operation, ...]:
        """Return every documented operation."""
        return tuple(self._operations.values())

    def operations_for(self, resource: str) -> set[str]:
        """Return operation names for a resource."""
        return {item.name for item in self.operation_list if item.resource == resource}

    def __getattr__(self, resource: str) -> Resource:
        if resource.startswith("_") or resource.replace("_", "-") not in self.resources:
            raise AttributeError(f"Unknown Nessus resource: {resource}")
        return Resource(self, resource.replace("_", "-"))

    def call(
        self,
        resource: str,
        operation: str,
        *,
        path: dict[str, JsonValue] | None = None,
        query: dict[str, JsonValue] | None = None,
        payload: dict[str, JsonValue] | None = None,
        body: JsonValue | None = None,
        file_path: str | Path | None = None,
        output_path: str | Path | None = None,
        **arguments: JsonValue,
    ) -> ResponseValue:
        """Call any documented operation using named or grouped parameters."""
        key = (resource, operation.replace("_", "-"))
        if key not in self._operations:
            raise NessusError(f"Unknown Nessus operation: {resource}.{operation}")
        item = self._operations[key]
        grouped = group_arguments(item, arguments, path, query, payload)
        request_parameters = item.definition.get("request", {}).get("parameters", {})
        body_definition = request_parameters.get("body", {}).get("Request Body", {})
        if body_definition.get("required") and body is None:
            raise NessusError("Missing required parameter: request_body")
        if (resource == "file" or item.name.endswith("upload")) and file_path is None:
            raise NessusError("Missing required parameter: file_path")
        url = build_url(self.config.base_url, item.uri, grouped.path, grouped.query)
        request_body: bytes | None
        content_type: str | None
        if file_path is not None:
            request_body, content_type = multipart(file_path, grouped.payload)
        else:
            request_body, content_type = json_body(item, grouped.payload, body)
        data = self._transport.request(item.method, url, request_body, content_type)
        if output_path is not None:
            return self._output_writer.write(output_path, data)
        return data
