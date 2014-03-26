#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return open(os.path.join(here, *parts), 'r').read()


readme = read('README.rst')
history = read('HISTORY.rst').replace('.. :changelog:', '')
requirements = read('requirements.txt')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='tox-matrix',
    version='0.1.1',
    description='Project for creating tox.ini files with multiple dependencies',
    long_description=readme + '\n\n' + history,
    author='Slawek Ehlert',
    author_email='slafs@op.pl',
    url='https://github.com/slafs/tox-matrix',
    packages=[
        'toxmatrix',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='tox-matrix',
    entry_points="""
    [console_scripts]
    tox-matrix = toxmatrix.cli:main
    """,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
