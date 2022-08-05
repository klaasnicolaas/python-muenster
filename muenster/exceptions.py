"""Asynchronous Python client providing Open Data information of Münster."""


class ODPMuensterError(Exception):
    """Generic Open Data Platform Münster exception."""


class ODPMuensterConnectionError(ODPMuensterError):
    """Open Data Platform Münster - connection error."""
