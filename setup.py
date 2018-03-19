#!/usr/bin/env python

from setuptools import setup, find_packages
import os

from btcp import __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = []

setup(name='python-btcplib',
      version=__version__,
      description='The Swiss Army Knife of the btcp protocol -- forked from python-bitcoinlib.',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
      ],
      url='https://github.com/petertodd/python-bitcoinlib',
      keywords='btcp',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires,
      test_suite="btcp.tests"
     )
