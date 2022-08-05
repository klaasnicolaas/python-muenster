"""Asynchronous Python client providing Open Data information of Münster."""
import os


def load_fixtures(filename: str) -> str:
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()
