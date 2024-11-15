"""Fixture for the Muenster tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from muenster import ODPMuenster, StadtMuenster


@pytest.fixture(name="odp_muenster_client")
async def odp_client() -> AsyncGenerator[ODPMuenster, None]:
    """Return an ODP Muenster client."""
    async with (
        ClientSession() as session,
        ODPMuenster(session=session) as odp_muenster_client,
    ):
        yield odp_muenster_client


@pytest.fixture(name="stadt_muenster_client")
async def stadt_client() -> AsyncGenerator[StadtMuenster, None]:
    """Return an Stadt Muenster client."""
    async with (
        ClientSession() as session,
        StadtMuenster(session=session) as stadt_muenster_client,
    ):
        yield stadt_muenster_client
