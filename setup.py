#! /usr/bin/env python
import os
import sys
import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension

try:
    import model_metadata
except ImportError:

    def get_cmdclass(*args, **kwds):
        return kwds.get("cmdclass", None)

    def get_entry_points(*args):
        return None


else:
    from model_metadata.utils import get_cmdclass, get_entry_points


packages = find_packages()
pymt_components = [
    ("InfilGreenAmpt=pymt_topoflow.bmi:InfilGreenAmpt", "meta/InfilGreenAmpt"),
    ("InfilRichards1D=pymt_topoflow.bmi:InfilRichards1D", "meta/InfilRichards1D"),
    (
        "InfilSmithParlange=pymt_topoflow.bmi:InfilSmithParlange",
        "meta/InfilSmithParlange",
    ),
]

setup(
    name="pymt_topoflow",
    author="Eric Hutton",
    description="PyMT plugin topoflow",
    version=versioneer.get_version(),
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
