"""Shared JSON and response types."""

type JsonValue = None | bool | int | float | str | list[JsonValue] | dict[
    str, JsonValue
]
type ResponseValue = JsonValue | bytes
