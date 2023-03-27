"""Models for Open Data Platform of Münster."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pyproj


@dataclass
class Garage:
    """Object representing a garage."""

    name: str
    status: str
    parking_type: str
    free_space: int
    total_capacity: int
    availability_pct: float
    url: str

    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls: type[Garage], data: dict[str, Any]) -> Garage:
        """Return a Garage object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A Garage object.
        """
        attr = data["properties"]
        geo = data["geometry"]["coordinates"]

        # Convert the coordinates from Guass-Kruger (zone 3) to WGS84.
        gauss_kruger_wgs = pyproj.Transformer.from_crs(31467, 4326)
        converted = gauss_kruger_wgs.transform(geo[1], geo[0])

        return cls(
            name=attr.get("NAME"),
            status=attr.get("status"),
            parking_type=attr.get("type"),
            free_space=attr.get("parkingFree"),
            total_capacity=attr.get("parkingTotal"),
            availability_pct=round(
                (float(attr.get("parkingFree")) / float(attr.get("parkingTotal")))
                * 100,
                1,
            ),
            url=attr.get("URL"),
            longitude=converted[1],
            latitude=converted[0],
        )
