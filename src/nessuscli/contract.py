"""Loading and indexing the bundled Nessus API contract."""

from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import files
from typing import Any


@dataclass(frozen=True, slots=True)
class Operation:
    """One operation from the published Nessus API contract."""

    resource: str
    name: str
    method: str
    uri: str
    definition: dict[str, Any]


def load_contract() -> dict[str, Any]:
    """Load the packaged API contract without exposing unrelated metadata."""
    raw = files("nessuscli").joinpath("api_spec.json").read_text(encoding="utf-8")
    return {"resources": json.loads(raw)["resources"]}


def index_operations(contract: dict[str, Any]) -> dict[tuple[str, str], Operation]:
    """Index operations by resource and documented name."""
    operations: dict[tuple[str, str], Operation] = {}
    for resource, resource_definition in contract["resources"].items():
        for name, definition in resource_definition.get("methods", {}).items():
            operations[(resource, name)] = Operation(
                resource, name, definition["method"], definition["uri"], definition
            )
    return operations
