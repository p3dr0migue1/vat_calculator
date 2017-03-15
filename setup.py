#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="vat_calculator",
    version="1.0",
    description="VAT calculator",
    long_description="Python command line VAT calculator",
    author="Pedro Curado",
    author_email="pedro.miguel@live.co.uk",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
