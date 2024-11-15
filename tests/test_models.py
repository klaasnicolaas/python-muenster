"""Test the models."""

from __future__ import annotations

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
    assert spaces == snapshot
