from __future__ import annotations

import os
from math import inf, nan
from pathlib import Path
from typing import Any

import pytest

from nessuscli.config import Settings
from nessuscli.config_sources import default_config_path
from nessuscli.errors import ConfigurationError


def test_defaults_and_explicit_values() -> None:
    settings = Settings.from_sources(
        base_url="http://example.test/",
        access_key="access",
        secret_key="secret",
        token="token",
        timeout=4,
        verify_ssl=False,
    )
    assert settings.base_url == "http://example.test"
    assert settings.access_key == "access"
    assert settings.secret_key == "secret"
    assert settings.token == "token"
    assert settings.timeout == 4
    assert settings.verify_ssl is False


def test_settings_repr_does_not_expose_credentials() -> None:
    settings = Settings(
        access_key="access-secret",
        secret_key="secret-secret",
        token="session-secret",
    )
    rendered = repr(settings)
    assert "access-secret" not in rendered
    assert "secret-secret" not in rendered
    assert "session-secret" not in rendered


@pytest.mark.parametrize(
    ("kwargs", "name"),
    [
        ({"access_key": "invalid\r\nvalue"}, "access_key"),
        ({"secret_key": "invalid\r\nvalue"}, "secret_key"),
        ({"token": "invalid\r\nvalue"}, "token"),
    ],
)
def test_credentials_reject_control_characters(
    kwargs: dict[str, Any], name: str
) -> None:
    with pytest.raises(ConfigurationError, match="control characters"):
        Settings.from_sources(**kwargs)


def test_credentials_reject_del_character() -> None:
    with pytest.raises(ConfigurationError, match="control characters"):
        Settings(access_key="invalid\x7fvalue", secret_key="secret")


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"base_url": "https://"}, "valid URL"),
        ({"base_url": ""}, "valid URL"),
        ({"base_url": "ftp://example.test"}, "start with"),
        ({"base_url": 1}, "must be a string"),
        ({"base_url": "https://example.test?query=value"}, "query or fragment"),
        ({"base_url": "https://example.test#fragment"}, "query or fragment"),
        ({"base_url": "https://example.test:invalid"}, "valid port"),
        ({"base_url": "https://[invalid"}, "valid URL"),
        ({"base_url": "https://:8834"}, "valid URL with a host"),
        ({"base_url": "https://example.test/\x00path"}, "control characters"),
        ({"access_key": "access"}, "provided together"),
        ({"access_key": 1, "secret_key": 1}, "must be a string"),
        ({"timeout": None}, "must be a number"),
        ({"timeout": nan}, "finite"),
        ({"timeout": inf}, "finite"),
        ({"verify_ssl": None}, "must be a boolean"),
    ],
)
def test_direct_settings_constructor_validates_invariants(
    kwargs: dict[str, Any], message: str
) -> None:
    with pytest.raises(ConfigurationError, match=message):
        Settings(**kwargs)


def test_config_file_and_environment_precedence(tmp_path: Path) -> None:
    config = tmp_path / "config.toml"
    config.write_text(
        "[nessus]\nbase_url = 'http://file.test'\n"
        "access_key = 'file-access'\nsecret_key = 'file-secret'\n"
        "timeout = 12\nverify_ssl = false\n",
        encoding="utf-8",
    )
    old = dict(os.environ)
    try:
        os.environ.update(
            {
                "NESSUS_BASE_URL": "http://env.test",
                "NESSUS_ACCESS_KEY": "env-access",
                "NESSUS_SECRET_KEY": "env-secret",
                "NESSUS_TIMEOUT": "8",
                "NESSUS_VERIFY_SSL": "true",
            }
        )
        settings = Settings.from_sources(
            config_path=config,
            base_url="http://cli.test",
            timeout=2,
            verify_ssl=False,
        )
        assert settings.base_url == "http://cli.test"
        assert settings.access_key == "env-access"
        assert settings.secret_key == "env-secret"
        assert settings.timeout == 2
        assert settings.verify_ssl is False
    finally:
        os.environ.clear()
        os.environ.update(old)


def test_empty_environment_base_url_is_rejected() -> None:
    old = os.environ.get("NESSUS_BASE_URL")
    try:
        os.environ["NESSUS_BASE_URL"] = ""
        with pytest.raises(ConfigurationError, match="valid URL"):
            Settings.from_sources()
    finally:
        if old is None:
            os.environ.pop("NESSUS_BASE_URL", None)
        else:
            os.environ["NESSUS_BASE_URL"] = old


def test_environment_config_path_and_token(tmp_path: Path) -> None:
    config = tmp_path / "config.toml"
    config.write_text(
        "base_url = 'http://configured.test'\ntoken = 'file-token'\n", encoding="utf-8"
    )
    old = dict(os.environ)
    try:
        os.environ.update({"NESSUS_CONFIG": str(config), "NESSUS_TOKEN": "env-token"})
        settings = Settings.from_sources()
        assert settings.base_url == "http://configured.test"
        assert settings.token == "env-token"
    finally:
        os.environ.clear()
        os.environ.update(old)


def test_default_config_path_is_platform_appropriate(tmp_path: Path) -> None:
    assert (
        default_config_path(
            system="nt",
            home=tmp_path,
            environment={"APPDATA": str(tmp_path / "AppData")},
        )
        == tmp_path / "AppData" / "nessuscli" / "config.toml"
    )
    assert (
        default_config_path(system="nt", home=tmp_path, environment={"APPDATA": ""})
        == tmp_path / "AppData" / "Roaming" / "nessuscli" / "config.toml"
    )
    assert (
        default_config_path(
            system="posix", platform="darwin", home=tmp_path, environment={}
        )
        == tmp_path / "Library" / "Application Support" / "nessuscli" / "config.toml"
    )
    assert (
        default_config_path(
            system="posix",
            platform="linux",
            home=tmp_path,
            environment={"XDG_CONFIG_HOME": str(tmp_path / "xdg")},
        )
        == tmp_path / "xdg" / "nessuscli" / "config.toml"
    )
    assert (
        default_config_path(
            system="posix",
            platform="linux",
            home=tmp_path,
            environment={"XDG_CONFIG_HOME": ""},
        )
        == tmp_path / ".config" / "nessuscli" / "config.toml"
    )


def test_missing_environment_config() -> None:
    old = os.environ.pop("NESSUS_CONFIG", None)
    try:
        os.environ["NESSUS_CONFIG"] = "/missing/config.toml"
        with pytest.raises(ConfigurationError, match="does not exist"):
            Settings.from_sources()
    finally:
        os.environ.pop("NESSUS_CONFIG", None)
        if old is not None:
            os.environ["NESSUS_CONFIG"] = old


def test_boolean_file_and_environment_values(tmp_path: Path) -> None:
    config = tmp_path / "config.toml"
    config.write_text("[nessus]\nverify_ssl = false\n", encoding="utf-8")
    assert Settings.from_sources(config_path=config).verify_ssl is False
    old = os.environ.get("NESSUS_VERIFY_SSL")
    try:
        os.environ["NESSUS_VERIFY_SSL"] = "true"
        assert Settings.from_sources().verify_ssl is True
        os.environ["NESSUS_VERIFY_SSL"] = "false"
        assert Settings.from_sources().verify_ssl is False
        os.environ["NESSUS_VERIFY_SSL"] = "invalid"
        with pytest.raises(ConfigurationError, match="must be a boolean"):
            Settings.from_sources()
    finally:
        if old is None:
            os.environ.pop("NESSUS_VERIFY_SSL", None)
        else:
            os.environ["NESSUS_VERIFY_SSL"] = old


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"config_path": "/missing/config.toml"}, "does not exist"),
        ({"access_key": "only"}, "provided together"),
        ({"base_url": "ftp://example.test"}, "start with"),
        ({"timeout": 0}, "greater than zero"),
        ({"timeout": "bad"}, "must be a number"),
        ({"verify_ssl": "bad"}, "must be a boolean"),
    ],
)
def test_invalid_explicit_configuration(kwargs: dict[str, Any], message: str) -> None:
    old_keys = {
        name: os.environ.pop(name, None)
        for name in ("NESSUS_ACCESS_KEY", "NESSUS_SECRET_KEY")
    }
    try:
        with pytest.raises(ConfigurationError, match=message):
            Settings.from_sources(**kwargs)
    finally:
        for name, value in old_keys.items():
            if value is not None:
                os.environ[name] = value


def test_invalid_toml_and_section(tmp_path: Path) -> None:
    invalid = tmp_path / "invalid.toml"
    invalid.write_text("not = [valid", encoding="utf-8")
    with pytest.raises(ConfigurationError, match="Invalid TOML"):
        Settings.from_sources(config_path=invalid)

    wrong = tmp_path / "wrong.toml"
    wrong.write_text("nessus = 'string'", encoding="utf-8")
    with pytest.raises(ConfigurationError, match="must be a table"):
        Settings.from_sources(config_path=wrong)

    wrong_type = tmp_path / "wrong-type.toml"
    wrong_type.write_text("[nessus]\nbase_url = 123\n", encoding="utf-8")
    with pytest.raises(ConfigurationError, match="base_url must be a string"):
        Settings.from_sources(config_path=wrong_type)
