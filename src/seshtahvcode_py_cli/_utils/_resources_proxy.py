from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `seshtahvcode_py_cli.resources` module.

    This is used so that we can lazily import `seshtahvcode_py_cli.resources` only when
    needed *and* so that users can just import `seshtahvcode_py_cli` and reference `seshtahvcode_py_cli.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("seshtahvcode_py_cli.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
