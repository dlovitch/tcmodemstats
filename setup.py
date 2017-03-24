#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = [
    'beautifulsoup4>=4.5.3',
    'click>=6.7',
    'lxml>=3.7.2',
    'python-dateutil>=2.6.0',
    'pytz>=2016.10',
    'PyYAML>=3.12',
    'requests>=2.13.0',
    ]

test_requirements = ['pytest>=3.0.7']

setup(
    name='tcmodemstats',
    version='1.0.0',
    description='Scrape statistics from Technicolor cable modems',
    author='David Lovitch',
    author_email='dlovitch@gmail.com',
    url='https://github.com/dlovitch/tcmodemstats/',
    packages=find_packages(),
    install_requires=requires,
    tests_require=test_requirements,
    extras_require={
        'influxdb': ['influxdb>=4.0.0'],
        'datadog': ['datadog>=0.15.0'],
    },
    entry_points={
        'console_scripts': [
            "tcmodemstatscli=tcmodemstats.cli:main",
            "tcmodemstatsforwarder=tcmodemstats.cli_forwarder:main",
        ],
    },

)
