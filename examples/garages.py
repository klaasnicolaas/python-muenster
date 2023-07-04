# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Münster."""

import asyncio

from muenster import StadtMuenster


async def main() -> None:
    """Show example on using the Münster API client."""
    async with StadtMuenster() as client:
        garages = await client.garages()

        count: int = len(garages)
        for item in garages:
            print(item)

        print("__________________________")
        print(f"Total locations found: {count}")


if __name__ == "__main__":
    asyncio.run(main())
