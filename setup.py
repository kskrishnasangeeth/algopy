#!/usr/bin/env python

from setuptools import setup

def readme():
    return open("README.rst").read()

setup(name='algopy',
      version='0.1.0',
      description=("Python package solutions to algorithm Problems"
                   "where questions are collected from various sources"),
      long_description=readme(),
      author='Krishna Sangeeth KS.',
      author_email='krishna@sangeeth.net',
      url='http://github.com/kskrishnasangeeth/AlgoPy',
      license="BSD 2-Clause",
      packages=['AlgoPy'],
      test_suite="tests",
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Games/Entertainment :: Puzzle Games',
      ])
