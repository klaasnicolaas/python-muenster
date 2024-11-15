"""Basic tests for the Open Data Platform API of Münster."""

# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from muenster import StadtMuenster
from muenster.exceptions import ODPMuensterConnectionError, ODPMuensterError

from . import load_fixtures


async def test_json_request(
    aresponses: ResponsesMockServer, stadt_muenster_client: StadtMuenster
) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "stadt-muenster.de",
        "/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "text/html"},
            text=load_fixtures("garages.json"),
        ),
    )
    await stadt_muenster_client._request("test")
    await stadt_muenster_client.close()


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is handled correctly."""
    aresponses.add(
        "stadt-muenster.de",
        "/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "text/html"},
            text=load_fixtures("garages.json"),
        ),
    )
    async with StadtMuenster() as client:
        await client._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout from the Open Data Platform API of Münster."""

    # Faking a timeout by sleeping
    async def response_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
            text=load_fixtures("garages.json"),
        )

    aresponses.add("stadt-muenster.de", "/test", "GET", response_handler)

    async with ClientSession() as session:
        client = StadtMuenster(
            session=session,
            request_timeout=0.1,
        )
        with pytest.raises(ODPMuensterConnectionError):
            assert await client._request("test")


async def test_content_type(
    aresponses: ResponsesMockServer, stadt_muenster_client: StadtMuenster
) -> None:
    """Test request content type error from Open Data Platform API of Münster."""
    aresponses.add(
        "stadt-muenster.de",
        "/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )
    with pytest.raises(ODPMuensterError):
        assert await stadt_muenster_client._request("test")


async def test_client_error() -> None:
    """Test request client error from the Open Data Platform API of Münster."""
    async with ClientSession() as session:
        client = StadtMuenster(session=session)
        with (
            patch.object(
                session,
                "request",
                side_effect=ClientError,
            ),
            pytest.raises(ODPMuensterConnectionError),
        ):
            assert await client._request("test")
