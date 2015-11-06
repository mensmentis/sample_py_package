#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-


__author__ = 'Mens Mentis'


from setuptools import setup, find_packages


setup(
    name="sample_py_package",
    version="0.0.1",
    description="testing system independency of setuptools",
    license="BSD",
    keywords="setuptools example",
    # packages=find_packages(exclude=['examples', 'docs']),
    # include_package_data=True,
    install_requires = ["matplotlib"],
)
