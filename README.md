<!-- Banner -->
![alt Banner of the ODP Muenster package](https://raw.githubusercontent.com/klaasnicolaas/python-muenster/main/assets/header_muenster-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

[![Code Quality][code-quality-shield]][code-quality]
[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]

[![Maintainability][maintainability-shield]][maintainability-url]
[![Code Coverage][codecov-shield]][codecov-url]

Asynchronous Python client for the open datasets of Münster (Germany).

## About

A python package with which you can retrieve data from the Open Data Platform of Münster via [their API][api]. This package was initially created to only retrieve parking data from the API, but the code base is made in such a way that it is easy to extend for other datasets from the same platform.

## Installation

```bash
pip install muenster
```

## Datasets

You can read the following datasets with this package:

- [Garages / Parkleitsystem][garages] (17 locations)

<details>
    <summary>Click here to get more details</summary>

### Garages

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `name` | string | The name of the garage |
| `status` | string | The status of the garage |
| `parking_type` | string | The type of parking of the garage (**Parkplatz** or **Parkhaus**) |
| `free_space` | integer | The free space of the garage |
| `total_capacity` | integer | The total capacity of the garage |
| `availability_pct` | float | The availability percentage of the garage |
| `url` | string | The URL with more information of the garage |
| `longitude` | float | The longitude of the garage |
| `latitude` | float | The latitude of the garage |
</details>

## Example

```python
import asyncio

from muenster import StadtMuenster


async def main() -> None:
    """Show example on using the API of Münster."""
    async with StadtMuenster() as client:
        garages = await client.garages(limit=10)
        print(garages)


if __name__ == "__main__":
    asyncio.run(main())
```

## Use cases

[NIPKaart.nl][nipkaart]

A website that provides insight into where disabled parking spaces are, based
on data from users and municipalities. Operates mainly in the Netherlands, but
also has plans to process data from abroad.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager.

You need at least:

- Python 3.9+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Setup the pre-commit check, you must run this inside the virtual environment:

```bash
pre-commit install
```

*Now you're all set to get started!*

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## License

MIT License

Copyright (c) 2022-2023 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[api]: https://opendata.stadt-muenster.de
[garages]: https://opendata.stadt-muenster.de/dataset/parkleitsystem-parkhausbelegung-aktuell
[nipkaart]: https://www.nipkaart.nl

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-muenster/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-muenster/actions/workflows/tests.yaml
[code-quality-shield]: https://github.com/klaasnicolaas/python-muenster/actions/workflows/codeql.yaml/badge.svg
[code-quality]: https://github.com/klaasnicolaas/python-muenster/actions/workflows/codeql.yaml
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-muenster.svg
[commits-url]: https://github.com/klaasnicolaas/python-muenster/commits/main
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-muenster/branch/main/graph/badge.svg?token=OZgV3Ib3Er
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-muenster
[downloads-shield]: https://img.shields.io/pypi/dm/muenster
[downloads-url]: https://pypistats.org/packages/muenster
[issues-shield]: https://img.shields.io/github/issues/klaasnicolaas/python-muenster.svg
[issues-url]: https://github.com/klaasnicolaas/python-muenster/issues
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-muenster.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-muenster.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/cb6cb45c337d037071b7/maintainability
[maintainability-url]: https://codeclimate.com/github/klaasnicolaas/python-muenster/maintainability
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/muenster/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/muenster
[typing-shield]: https://github.com/klaasnicolaas/python-muenster/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-muenster/actions/workflows/typing.yaml
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-muenster.svg
[releases]: https://github.com/klaasnicolaas/python-muenster/releases
[stars-shield]: https://img.shields.io/github/stars/klaasnicolaas/python-muenster.svg
[stars-url]: https://github.com/klaasnicolaas/python-muenster/stargazers

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
