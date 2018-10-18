#! /usr/bin/env python

from .bmi import InfilGreenAmpt, InfilRichards1D, InfilSmithParlange

__all__ = ["InfilGreenAmpt", "InfilRichards1D", "InfilSmithParlange"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
