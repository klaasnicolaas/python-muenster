"""Test the models."""

from __future__ import annotations

from dataclasses import replace
from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from muenster import Garage, StadtMuenster


async def test_all_garages(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    stadt_muenster_client: StadtMuenster,
) -> None:
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
    spaces: list[Garage] = await stadt_muenster_client.garages()
    # Ignore platform-specific PROJ rounding below submillimeter precision.
    assert [
        replace(
            space,
            latitude=round(space.latitude, 9),
            longitude=round(space.longitude, 9),
        )
        for space in spaces
    ] == snapshot
