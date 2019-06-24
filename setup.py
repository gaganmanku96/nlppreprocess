# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

# To upload this file to PyPI you must build it then upload it:
# python setup.py sdist bdist_wheel  # build in 'dist' folder
# python-m twine upload dist/*  # 'twine' must be installed: 'pip install twine'


import ast
import io
import re
import os
from setuptools import find_packages, setup

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="nlppreprocess",
    version="1.0.1",
    author="Gagandeep Singh",
    author_email="gaganmanku96@gmail.com",
    description="This package contains preprocessing functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gaganmanku96/nlppreprocess",
    include_package_data=True,
    zip_safe=False,
    test_suite="tests.test_project",
    packages=["nlppreprocess"],
    python_requires=">=3.4",
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
