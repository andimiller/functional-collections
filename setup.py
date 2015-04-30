# encoding: utf-8

from setuptools import setup
import os.path

setup(
    name="functional_collections",
    version="0.0.1",
    author="andimiller",
    author_email="andi at andimiller dot net",
    maintainer="andimiller",
    maintainer_email="andi at andimiller dot net",
    description="Collection of tools for functional composition in Python.",
    long_description = os.path.isfile("README.md") and open('README.md').read() or None,
    license=(
        "Copyright (C) 2014-Present Andi Miller"
        "All Rights Reserved. "
        "See LICENSE for the full license."
    ),
    url="https://github.com/andimiller/functional-collections",
    packages=['functional_collections'],
    install_requires=[
	'forbiddenfruit',
	'six'
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
