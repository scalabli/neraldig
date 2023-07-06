#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="neuraldig",
    install_requires=[
        "numpy==1.21.0",
        "scipy==1.10.0",
        "pandas==1.0",
        "scikit-learn==0.22",
        "joblib==0.15",
        "nibabel==3.0.0",
        "lxml",
        "quo",
    ],
)
