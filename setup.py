# coding=utf-8

from setuptools import setup, find_packages

NAME = "krakenio"
VERSION = "0.2.0"
DESCRIPTION = "Kraken.io API Client"
LONG_DESCRIPTION = (
    "Official Python client for integrating with the Kraken.io Image Optimizer, "
    "providing fast and powerful image optimization capabilities."
)
URL = "https://github.com/kraken-io/kraken-python"
AUTHOR = "Nekkra UG"
AUTHOR_EMAIL = "support@kraken.io"
LICENSE = "MIT"
KEYWORDS = ["kraken", "kraken.io", "image", "optimizer", "resizer"]

INSTALL_REQUIRES = [
    "requests>=2.28.0",
    "urllib3<2.0",  
]

EXTRAS_REQUIRE = {
    "test": [
        "python-dotenv>=1.0.0",
    ],
}

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8", 
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

required_fields = {
    "name": NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "long_description": LONG_DESCRIPTION,
    "long_description_content_type": "text/plain",
    "url": URL,
    "author": AUTHOR,
    "author_email": AUTHOR_EMAIL,
    "license": LICENSE,
    "packages": find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    "install_requires": INSTALL_REQUIRES,
    "extras_require": EXTRAS_REQUIRE,
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
    "python_requires": ">=3.8", 
}

for field_name, field_value in required_fields.items():
    if not field_value:
        raise ValueError(f"Missing required field: {field_name}")

setup(**required_fields)