#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="dusk",
    version="0.1.0",
    packages=[
        "dusk"
    ],
    package_dir={
        "dusk": "dusk"
    },
    entry_points={
        "console_scripts": [
            "dusk=dusk.cli:cli"
        ]
    },
)
