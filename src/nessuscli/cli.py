"""Command-line interface for every operation in the Nessus API contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Sequence

from .client import NessusClient
from .config import Settings
from .contract import load_contract
from .errors import NessusError
from .factory import create_client

_MISSING = object()


def main(argv: Sequence[str] | None = None) -> int:
    """Run the ``nessus`` command and return a process exit code."""
    parser = _parser()
    args = parser.parse_args(argv)
    try:
        settings = Settings.from_sources(
            config_path=args.config,
            base_url=args.base_url,
            access_key=args.access_key,
            secret_key=args.secret_key,
            token=args.token,
            timeout=args.timeout,
            verify_ssl=False if args.insecure else None,
        )
        client = create_client(settings)
        if args.command == "resources":
            print(json.dumps(_resource_index(client), indent=2))
            return 0
        if args.command == "call":
            resource = args.resource
            operation = args.operation
        else:
            resource = args.api_resource
            operation = args.api_operation
        arguments = _parse_arguments(args.argument)
        arguments.update(_named_options(args))
        result = client.call(
            resource,
            operation,
            path=_json_object(args.path, "path"),
            query=_json_object(args.query, "query"),
            payload=_json_object(args.payload, "payload"),
            body=json.loads(args.body) if args.body is not None else None,
            file_path=args.file,
            output_path=args.output,
            **arguments,
        )
        _print_result(result)
        return 0
    except (NessusError, ValueError, OSError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nessus",
        description="Call any operation in the Nessus REST API.",
    )
    parser.add_argument("--config", type=Path, help="TOML config file")
    parser.add_argument("--base-url", help="Nessus base URL")
    parser.add_argument("--access-key", help="Nessus API access key")
    parser.add_argument("--secret-key", help="Nessus API secret key")
    parser.add_argument("--token", help="Nessus session token")
    parser.add_argument("--timeout", type=float, help="HTTP timeout in seconds")
    parser.add_argument(
        "--insecure", action="store_true", help="Disable TLS verification"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("resources", help="List all resources and operations")
    call = commands.add_parser("call", help="Call a resource operation")
    call.add_argument("resource")
    call.add_argument("operation")
    _add_call_options(call)
    for resource, definition in load_contract()["resources"].items():
        resource_parser = commands.add_parser(
            resource, help=f"Operations for the {resource} resource"
        )
        operation_commands = resource_parser.add_subparsers(
            dest="api_operation", required=True
        )
        for name, operation in definition.get("methods", {}).items():
            operation_parser = operation_commands.add_parser(
                name, help=_operation_help(operation)
            )
            operation_parser.set_defaults(api_resource=resource, api_operation=name)
            _add_call_options(operation_parser, operation)
    return parser


def _add_call_options(
    parser: argparse.ArgumentParser, operation: dict[str, Any] | None = None
) -> None:
    parser.add_argument("--path", help="Path parameters as a JSON object")
    parser.add_argument("--query", help="Query parameters as a JSON object")
    parser.add_argument("--payload", help="JSON payload object")
    parser.add_argument("--body", help="Raw JSON request body")
    parser.add_argument("--file", type=Path, help="File to upload")
    parser.add_argument(
        "--output", type=Path, help="Destination for a downloaded response"
    )
    parser.add_argument(
        "--arg",
        dest="argument",
        action="append",
        default=[],
        metavar="NAME=VALUE",
        help="Named parameter; VALUE is parsed as JSON when possible",
    )
    if operation is None:
        return
    parameter_specs: list[tuple[str, str]] = []
    used_options = {"arg", "body", "file", "output", "path", "payload", "query"}
    parameters = operation.get("request", {}).get("parameters", {})
    parameter_names = list(
        dict.fromkeys(
            [
                name
                for category in ("path", "query", "payload")
                for name in parameters.get(category, {})
            ]
            + re.findall(r"{([^{}]+)}", str(operation.get("uri", "")))
        )
    )
    for name in parameter_names:
        option = _unique_option_name(name, used_options)
        destination = f"_api_parameter_{len(parameter_specs)}"
        parser.add_argument(
            option,
            dest=destination,
            default=_MISSING,
            type=_parse_value,
            metavar="VALUE",
            help=f"API parameter {name}",
        )
        parameter_specs.append((destination, name))
    parser.set_defaults(api_parameter_specs=parameter_specs)


def _operation_help(operation: dict[str, Any]) -> str:
    description = str(operation.get("description", "")).strip()
    return re.sub(r"<[^>]+>", "", description) or "Call this API operation"


def _unique_option_name(name: str, used_options: set[str]) -> str:
    base = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    base = base or "parameter"
    candidate = base
    counter = 2
    while candidate in used_options:
        candidate = f"{base}-{counter}"
        counter += 1
    used_options.add(candidate)
    return f"--{candidate}"


def _named_options(args: argparse.Namespace) -> dict[str, Any]:
    return {
        name: getattr(args, destination)
        for destination, name in getattr(args, "api_parameter_specs", [])
        if getattr(args, destination) is not _MISSING
    }


def _json_object(value: str | None, name: str) -> dict[str, Any] | None:
    if value is None:
        return None
    parsed = json.loads(value)
    if not isinstance(parsed, dict):
        raise ValueError(f"--{name} must contain a JSON object")
    return parsed


def _parse_arguments(values: list[str]) -> dict[str, Any]:
    arguments: dict[str, Any] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"Invalid --arg value: {value}; expected NAME=VALUE")
        name, raw = value.split("=", 1)
        if not name:
            raise ValueError("--arg name cannot be empty")
        arguments[name] = _parse_value(raw)
    return arguments


def _parse_value(raw: str) -> Any:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def _resource_index(client: NessusClient) -> dict[str, list[str]]:
    return {
        resource: sorted(client.operations_for(resource))
        for resource in client.resources
    }


def _print_result(result: Any) -> None:
    if isinstance(result, bytes):
        sys.stdout.buffer.write(result)
    elif isinstance(result, str):
        print(result)
    else:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
