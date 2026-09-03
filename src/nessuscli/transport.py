"""HTTP transport for the Nessus client."""

from __future__ import annotations

import ssl
from urllib.error import HTTPError, URLError
from urllib.request import HTTPSHandler, Request, build_opener

from .config import Settings
from .errors import ApiError, NessusError
from .response import decode_response
from .types import ResponseValue


class UrllibTransport:
    """Cross-platform urllib implementation of the HTTP boundary."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def request(
        self, method: str, url: str, body: bytes | None, content_type: str | None
    ) -> ResponseValue:
        headers = {"Accept": "application/json"}
        if self._settings.access_key and self._settings.secret_key:
            headers["X-ApiKeys"] = (
                f"accessKey={self._settings.access_key}; "
                f"secretKey={self._settings.secret_key};"
            )
        if self._settings.token:
            headers["X-Cookie"] = f"token={self._settings.token};"
        if content_type:
            headers["Content-Type"] = content_type
        request_method = "GET" if method == "DOWNLOAD" else method
        request = Request(url, data=body, headers=headers, method=request_method)
        try:
            opener = build_opener(HTTPSHandler(context=_ssl_context(self._settings)))
            with opener.open(request, timeout=self._settings.timeout) as response:
                raw = response.read()
                if method == "DOWNLOAD":
                    return raw
                return decode_response(raw, response.headers.get("Content-Type", ""))
        except HTTPError as error:
            try:
                raw = error.read().decode("utf-8", errors="replace")
            finally:
                error.close()
            raise ApiError(error.code, error.reason, raw) from error
        except URLError as error:
            raise NessusError(f"Unable to reach Nessus: {error.reason}") from error


def _ssl_context(settings: Settings) -> ssl.SSLContext | None:
    if settings.verify_ssl:
        return None
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context
