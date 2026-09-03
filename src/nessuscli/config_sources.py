"""Configuration source loading and value normalization."""

from __future__ import annotations

import os
import sys
import tomllib
from collections.abc import Mapping
from math import isfinite
from pathlib import Path
from typing import Any

from .errors import ConfigurationError


def config_path(config_path: str | Path | None) -> Path | None:
    """Resolve an explicit, environment, or platform-default config path."""
    if config_path is not None:
        path = Path(config_path).expanduser()
        if not path.is_file():
            raise ConfigurationError(f"Config file does not exist: {path}")
        return path
    configured = os.getenv("NESSUS_CONFIG")
    if configured:
        path = Path(configured).expanduser()
        if not path.is_file():
            raise ConfigurationError(f"Config file does not exist: {path}")
        return path
    default = default_config_path()
    return default if default.is_file() else None


def default_config_path(
    *,
    system: str = os.name,
    platform: str = sys.platform,
    home: Path | None = None,
    environment: Mapping[str, str] | None = None,
) -> Path:
    """Return the platform-appropriate default configuration path."""
    home_path = home or Path.home()
    values = os.environ if environment is None else environment
    if system == "nt":
        configured_root = values.get("APPDATA")
        root = (
            Path(configured_root)
            if configured_root
            else home_path / "AppData" / "Roaming"
        )
    elif platform == "darwin":
        root = home_path / "Library" / "Application Support"
    else:
        configured_root = values.get("XDG_CONFIG_HOME")
        root = Path(configured_root) if configured_root else home_path / ".config"
    return root / "nessuscli" / "config.toml"


def read_config(path: Path | None) -> dict[str, Any]:
    """Read the selected TOML config section."""
    if path is None:
        return {}
    try:
        with path.open("rb") as config_file:
            loaded = tomllib.load(config_file)
    except tomllib.TOMLDecodeError as error:
        raise ConfigurationError(f"Invalid TOML config: {path}") from error
    section = loaded.get("nessus", loaded)
    if not isinstance(section, dict):
        raise ConfigurationError("The [nessus] config section must be a table")
    return section


def configured_value(
    explicit: str | None, environment: str | None, values: dict[str, Any], name: str
) -> str | None:
    """Resolve a string from explicit, environment, and file sources."""
    if explicit is not None:
        return explicit
    if environment is not None:
        return environment
    configured = values.get(name)
    if configured is None:
        return None
    if not isinstance(configured, str):
        raise ConfigurationError(f"{name} must be a string")
    return configured


def number_value(
    explicit: float | None,
    environment: str | None,
    values: dict[str, Any],
    name: str,
    default: float,
) -> float:
    """Resolve and validate a positive finite number."""
    value: Any = explicit
    if value is None:
        value = environment if environment is not None else values.get(name, default)
    try:
        result = float(value)
    except (TypeError, ValueError) as error:
        raise ConfigurationError(f"{name} must be a number") from error
    if isinstance(value, bool) or not isfinite(result):
        raise ConfigurationError(f"{name} must be finite")
    if result <= 0:
        raise ConfigurationError(f"{name} must be greater than zero")
    return result


def boolean_value(
    explicit: bool | None,
    environment: str | None,
    values: dict[str, Any],
    name: str,
    default: bool,
) -> bool:
    """Resolve and validate a boolean value."""
    if explicit is not None:
        if not isinstance(explicit, bool):
            raise ConfigurationError(f"{name} must be a boolean")
        return explicit
    value: Any = environment if environment is not None else values.get(name, default)
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.lower() in {"true", "1", "yes"}:
        return True
    if isinstance(value, str) and value.lower() in {"false", "0", "no"}:
        return False
    raise ConfigurationError(f"{name} must be a boolean")
