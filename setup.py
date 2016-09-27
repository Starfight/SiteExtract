#!/usr/bin/python
# -*- coding: utf8 -*-

# Copyright 2016 Nicolas DRUFIN

try:
    from setuptools import setup
    setup  # workaround for pyflakes issue #13
except ImportError:
    from distutils.core import setup

from site_extract import __version__

requirements = "PyMySQL"

setup(
    name='SiteExtract',
    version=__version__,
    author='Nicolas DRUFIN',
    author_email='nicolas.drufin@ensc.fr',
    packages=[
        'site_extract',
        'site_extract.database',
        'site_extract.messages',
        'site_extract.site'
    ],
    scripts=['bin/siteextract.py'],
    url='https://github.com/Starfight/SiteExtract',
    description='Collect data from websites',
    install_requires=requirements,
)