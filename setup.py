#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

setup(
    name="baltradutils",
    version="0.1",
    packages=find_namespace_packages(where="src", include=["baltradutils*"]),
    package_dir={"": "src"},
    namespace_packages=["baltradutils"],
    package_data={"": ["*.sql", "*.cfg"]},
    install_requires=[], 
    zip_safe=False,
)