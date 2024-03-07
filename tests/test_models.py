"""Test the models."""

from __future__ import annotations

from aiohttp import ClientSession
from aresponses import ResponsesMockServer

from muenster import Garage, StadtMuenster

from . import load_fixtures


async def test_all_garages(aresponses: ResponsesMockServer) -> None:
    """Test all garages function."""
    aresponses.add(
        "stadt-muenster.de",
        "/index.php",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "text/html"},
            text=load_fixtures("garages.json"),
        ),
    )
    async with ClientSession() as session:
        client = StadtMuenster(session=session)
        spaces: list[Garage] = await client.garages()
        assert spaces is not None
        for item in spaces:
            assert isinstance(item, Garage)
            assert item.url is not None
            assert item.longitude is not None
            assert item.latitude is not None
            assert isinstance(item.longitude, float)
            assert isinstance(item.latitude, float)
