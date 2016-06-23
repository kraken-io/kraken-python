# coding=utf-8

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup (
    name = 'krakenio',
    version = '0.0.2',
    description = 'Kraken.io API Client',
    long_description = 'With this official Python client you can plug into the power and speed of Kraken.io Image Optimizer.',
    url = 'https://github.com/kraken-io/kraken-python',
    author = 'Nekkra UG',
    author_email = 'support@kraken.io',
    license = 'MIT',
    keywords = 'kraken kraken.io image optimizer optimiser resizer',

    packages = [
        'krakenio'
    ],

    install_requires = [
        'requests'
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)