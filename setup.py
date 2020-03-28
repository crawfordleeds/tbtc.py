#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import Command, find_packages, setup

# Package metadata.
NAME = "tbtc"

DESCRIPTION = "Python bindings for tBTC."

# What packages are required for this module to be executed?
REQUIRED = ["web3"]

# What packages are optional?
EXTRAS = {
    "dev": ["bumpversion", "pytest>=4.4.0,<5.0.0", "nose2", "mypy", "isort", "black"]
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Where the magic happens:
setup(
    name="tbtc",
    version="0.1.0b0",  # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Crawford Leeds",
    author_email="crawford@crawfordleeds.com",
    python_requires=">=3.6.0",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
