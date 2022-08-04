"""Asynchronous Python client providing Open Data information of Muenster."""


class ODPMuensterError(Exception):
    """Generic Open Data Platform Muenster exception."""


class ODPMuensterConnectionError(ODPMuensterError):
    """Open Data Platform Muenster - connection error."""
