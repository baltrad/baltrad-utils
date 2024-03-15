#!/usr/bin/env python
import setuptools

import sys

REQUIRED_PACKAGES = [
]

setuptools.setup(
    name="baltradutils",
    version="0.1",
    namespace_packages=["baltradutils"],
    setup_requires=[],
    packages=setuptools.find_packages(
        "src",
    ),
    package_dir={
        "": "src"
    },
    package_data={
        "": ["*.sql", "*.cfg"]
    },
    install_requires=REQUIRED_PACKAGES,
    entry_points={
    },
    test_suite="nose.collector",
    tests_require=[
        "mock >= 0.7",
    ],
)
