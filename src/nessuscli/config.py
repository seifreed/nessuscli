"""Configuration loading from TOML files, environment, and CLI overrides."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlsplit

from .config_sources import (
    boolean_value,
    configured_value,
    number_value,
    read_config,
)
from .config_sources import (
    config_path as resolve_config_path,
)
from .errors import ConfigurationError

_DEFAULT_BASE_URL = "https://localhost:8834"
_DEFAULT_TIMEOUT = 30.0
_DEFAULT_VERIFY_SSL = True


@dataclass(frozen=True, slots=True)
class Settings:
    """Connection settings for a Nessus server."""

    base_url: str = _DEFAULT_BASE_URL
    access_key: str | None = field(default=None, repr=False)
    secret_key: str | None = field(default=None, repr=False)
    token: str | None = field(default=None, repr=False)
    timeout: float = _DEFAULT_TIMEOUT
    verify_ssl: bool = _DEFAULT_VERIFY_SSL

    def __post_init__(self) -> None:
        """Keep direct construction subject to the same input invariants."""
        if self.timeout is None:
            raise ConfigurationError("timeout must be a number")
        if self.verify_ssl is None:
            raise ConfigurationError("verify_ssl must be a boolean")
        _validate_credentials(self.access_key, self.secret_key, self.token)
        object.__setattr__(
            self,
            "base_url",
            _validate(self.base_url, self.access_key, self.secret_key),
        )
        object.__setattr__(
            self,
            "timeout",
            number_value(self.timeout, None, {}, "timeout", _DEFAULT_TIMEOUT),
        )
        object.__setattr__(
            self,
            "verify_ssl",
            boolean_value(
                self.verify_ssl,
                None,
                {},
                "verify_ssl",
                _DEFAULT_VERIFY_SSL,
            ),
        )

    @classmethod
    def from_sources(
        cls,
        *,
        config_path: str | Path | None = None,
        base_url: str | None = None,
        access_key: str | None = None,
        secret_key: str | None = None,
        token: str | None = None,
        timeout: float | None = None,
        verify_ssl: bool | None = None,
    ) -> Settings:
        """Load TOML, environment, and explicit values in that precedence order."""
        path = resolve_config_path(config_path)
        values = read_config(path)
        configured_base_url = configured_value(
            base_url, os.getenv("NESSUS_BASE_URL"), values, "base_url"
        )
        if configured_base_url is None:
            configured_base_url = _DEFAULT_BASE_URL
        configured_access_key = configured_value(
            access_key, os.getenv("NESSUS_ACCESS_KEY"), values, "access_key"
        )
        configured_secret_key = configured_value(
            secret_key, os.getenv("NESSUS_SECRET_KEY"), values, "secret_key"
        )
        configured_token = configured_value(
            token, os.getenv("NESSUS_TOKEN"), values, "token"
        )
        configured_timeout = number_value(
            timeout, os.getenv("NESSUS_TIMEOUT"), values, "timeout", _DEFAULT_TIMEOUT
        )
        configured_verify_ssl = boolean_value(
            verify_ssl,
            os.getenv("NESSUS_VERIFY_SSL"),
            values,
            "verify_ssl",
            _DEFAULT_VERIFY_SSL,
        )
        _validate_credentials(
            configured_access_key,
            configured_secret_key,
            configured_token,
        )
        normalized_base_url = _validate(
            configured_base_url,
            configured_access_key,
            configured_secret_key,
        )
        return cls(
            base_url=normalized_base_url,
            access_key=configured_access_key,
            secret_key=configured_secret_key,
            token=configured_token,
            timeout=configured_timeout,
            verify_ssl=configured_verify_ssl,
        )


def _validate(base_url: str, access_key: str | None, secret_key: str | None) -> str:
    if not isinstance(base_url, str):
        raise ConfigurationError("base_url must be a string")
    if any(ord(character) < 32 or ord(character) == 127 for character in base_url):
        raise ConfigurationError("base_url must not contain control characters")
    if bool(access_key) != bool(secret_key):
        raise ConfigurationError("access_key and secret_key must be provided together")
    base_url = base_url.strip()
    if not base_url:
        raise ConfigurationError("base_url must be a valid URL")
    try:
        parsed = urlsplit(base_url)
    except ValueError as error:
        raise ConfigurationError("base_url must be a valid URL") from error
    if parsed.scheme not in {"http", "https"}:
        raise ConfigurationError("base_url must start with http:// or https://")
    if not parsed.hostname:
        raise ConfigurationError("base_url must be a valid URL with a host")
    if parsed.query or parsed.fragment:
        raise ConfigurationError("base_url must not contain a query or fragment")
    try:
        parsed.port
    except ValueError as error:
        raise ConfigurationError("base_url must contain a valid port") from error
    return base_url.rstrip("/")


def _validate_credentials(
    access_key: str | None,
    secret_key: str | None,
    token: str | None,
) -> None:
    for name, value in (
        ("access_key", access_key),
        ("secret_key", secret_key),
        ("token", token),
    ):
        if value is not None and not isinstance(value, str):
            raise ConfigurationError(f"{name} must be a string")
        if value is not None and any(
            ord(character) < 32 or ord(character) == 127 for character in value
        ):
            raise ConfigurationError(f"{name} must not contain control characters")
