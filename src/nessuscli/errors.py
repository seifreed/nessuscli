"""Exceptions raised by nessuscli."""


class NessusError(Exception):
    """Base exception for client and configuration failures."""


class ConfigurationError(NessusError):
    """Raised when client configuration is missing or invalid."""


class ApiError(NessusError):
    """Raised when Nessus returns an HTTP error response."""

    def __init__(self, status_code: int, message: str, body: str = "") -> None:
        self.status_code = status_code
        self.body = body
        super().__init__(f"Nessus API returned HTTP {status_code}: {message}")
