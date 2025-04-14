"""Constants for sources."""

import pystow

__all__ = [
    "MODULE",
    "get_module",
]

MODULE = pystow.module("bio", "biognosis")


def get_module(key: str, *, version: str | None = None) -> pystow.Module:
    """Get the module."""
    rv = MODULE.module(key)
    if version is not None:
        rv = rv.module(version)
    return rv
