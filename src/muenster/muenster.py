"""Asynchronous Python client providing Open Data information of Münster."""
from __future__ import annotations

import asyncio
import json
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, cast

import async_timeout
from aiohttp import ClientError, ClientSession
from aiohttp.hdrs import METH_GET
from yarl import URL

from .exceptions import ODPMuensterConnectionError, ODPMuensterError
from .models import Garage


@dataclass
class ODPMuenster:
    """Main class for handling data fetchting from Open Data Platform of Münster."""

    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Open Data Platform API of Münster.

        Args:
        ----
            uri: Request URI, without '/', for example, 'status'
            method: HTTP method to use, for example, 'GET'
            params: Extra options to improve or limit the response.

        Returns:
        -------
            A Python dictionary (text) with the response from
            the Open Data Platform API of Münster.

        Raises:
        ------
            ODPMuensterConnectionError: Timeout occurred while
                connecting to the Open Data Platform API.
            ODPMuensterError: If the data is not valid.
        """
        version = metadata.version(__package__)
        url = URL.build(
            scheme="https",
            host="opendata.stadt-muenster.de",
            path="/dataset/",
        ).join(URL(uri))

        headers = {
            "Accept": "application/json",
            "User-Agent": f"PythonODPMuenster/{version}",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with async_timeout.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    ssl=True,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to the Open Data Platform API."
            raise ODPMuensterConnectionError(
                msg,
            ) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while communicating with Open Data Platform API."
            raise ODPMuensterConnectionError(
                msg,
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            msg = "Unexpected content type response from the Open Data Platform API"
            raise ODPMuensterError(
                msg,
                {"Content-Type": content_type, "Response": text},
            )

        return cast(dict[str, Any], await response.json())

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> ODPMuenster:
        """Async enter.

        Returns
        -------
            The Open Data Platform Münster object.
        """
        return self

    async def __aexit__(self, *_exc_info: Any) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.
        """
        await self.close()


@dataclass
class StadtMuenster:
    """Main class for handling data fetchting from Stadt of Münster."""

    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Open Data Platform API of Münster.

        Args:
        ----
            uri: Request URI, without '/', for example, 'status'
            method: HTTP method to use, for example, 'GET'
            params: Extra options to improve or limit the response.

        Returns:
        -------
            A Python dictionary (text) with the response from
            the Open Data Platform API of Münster.

        Raises:
        ------
            ODPMuensterConnectionError: Timeout occurred while
                connecting to the Open Data Platform API.
            ODPMuensterError: If the data is not valid.
        """
        version = metadata.version(__package__)
        url = URL.build(scheme="https", host="stadt-muenster.de", path="/").join(
            URL(uri),
        )

        headers = {
            "Accept": "text/html",
            "User-Agent": f"PythonStadtMuenster/{version}",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with async_timeout.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    ssl=True,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to the Open Data Platform API."
            raise ODPMuensterConnectionError(
                msg,
            ) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while communicating with Open Data Platform API."
            raise ODPMuensterConnectionError(
                msg,
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            text = await response.text()
            msg = "Unexpected content type response from the Open Data Platform API"
            raise ODPMuensterError(
                msg,
                {"Content-Type": content_type, "Response": text},
            )

        return json.loads(await response.text())

    async def garages(self) -> list[Garage]:
        """Get list of parking garages.

        Returns
        -------
            A list of Garage objects.
        """
        results: list[Garage] = []
        locations = await self._request(
            "index.php",
            params={"id": "10910"},
        )

        for item in locations["features"]:
            results.append(Garage.from_dict(item))
        return results

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> StadtMuenster:
        """Async enter.

        Returns
        -------
            The Stadt Münster object.
        """
        return self

    async def __aexit__(self, *_exc_info: Any) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.
        """
        await self.close()
