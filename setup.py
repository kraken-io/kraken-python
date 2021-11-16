# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from krakenio.meta import KrakenioMeta

setup(
    name = KrakenioMeta.name,
    version = KrakenioMeta.version,
    description = KrakenioMeta.description,
    long_description = KrakenioMeta.long_description,
    url = KrakenioMeta.url,
    author = KrakenioMeta.author,
    author_email = KrakenioMeta.author_email,
    license = KrakenioMeta.license,
    keywords = KrakenioMeta.keywords,
    packages = KrakenioMeta.packages,
    install_requires = KrakenioMeta.install_requires,
    classifiers = KrakenioMeta.classifiers
)
