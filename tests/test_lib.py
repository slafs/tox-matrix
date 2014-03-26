#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_lib
----------------------------------

Tests for `toxmatrix.lib` module.
"""

from toxmatrix.lib import generate_matrix, pin_version


def test_generate_matrix():

    python_versions = ['2.7', '3.3']
    packages = ['Django', 'Fabric']
    version_steps = [['1.5', '1.6', '1.7'], ['1.5', '1.6', '1.7', '1.8']]
    pin_exact = False

    ret = generate_matrix(python_versions, packages, version_steps, pin_exact)

    expected = (
        ('python2.7',
            (
                ('Django>=1.5,<1.6', 'Fabric>=1.5,<1.6'),
                ('Django>=1.5,<1.6', 'Fabric>=1.6,<1.7'),
                ('Django>=1.5,<1.6', 'Fabric>=1.7,<1.8'),
                ('Django>=1.6,<1.7', 'Fabric>=1.5,<1.6'),
                ('Django>=1.6,<1.7', 'Fabric>=1.6,<1.7'),
                ('Django>=1.6,<1.7', 'Fabric>=1.7,<1.8'),
            )
         ),
        ('python3.3',
            (
                ('Django>=1.5,<1.6', 'Fabric>=1.5,<1.6'),
                ('Django>=1.5,<1.6', 'Fabric>=1.6,<1.7'),
                ('Django>=1.5,<1.6', 'Fabric>=1.7,<1.8'),
                ('Django>=1.6,<1.7', 'Fabric>=1.5,<1.6'),
                ('Django>=1.6,<1.7', 'Fabric>=1.6,<1.7'),
                ('Django>=1.6,<1.7', 'Fabric>=1.7,<1.8'),
            )
         )
    )

    assert ret == expected


def test_generate_matrix_exact():

    python_versions = ['2.7', '3.3']
    packages = ['Django', 'Fabric']
    version_steps = [['1.5', '1.6', '1.7'], ['1.5', '1.6', '1.7', '1.8']]
    pin_exact = True

    ret = generate_matrix(python_versions, packages, version_steps, pin_exact)

    expected = (
        ('python2.7',
            (
                ('Django==1.5', 'Fabric==1.5'),
                ('Django==1.5', 'Fabric==1.6'),
                ('Django==1.5', 'Fabric==1.7'),
                ('Django==1.5', 'Fabric==1.8'),
                ('Django==1.6', 'Fabric==1.5'),
                ('Django==1.6', 'Fabric==1.6'),
                ('Django==1.6', 'Fabric==1.7'),
                ('Django==1.6', 'Fabric==1.8'),
                ('Django==1.7', 'Fabric==1.5'),
                ('Django==1.7', 'Fabric==1.6'),
                ('Django==1.7', 'Fabric==1.7'),
                ('Django==1.7', 'Fabric==1.8'),
            )
         ),
        ('python3.3',
            (
                ('Django==1.5', 'Fabric==1.5'),
                ('Django==1.5', 'Fabric==1.6'),
                ('Django==1.5', 'Fabric==1.7'),
                ('Django==1.5', 'Fabric==1.8'),
                ('Django==1.6', 'Fabric==1.5'),
                ('Django==1.6', 'Fabric==1.6'),
                ('Django==1.6', 'Fabric==1.7'),
                ('Django==1.6', 'Fabric==1.8'),
                ('Django==1.7', 'Fabric==1.5'),
                ('Django==1.7', 'Fabric==1.6'),
                ('Django==1.7', 'Fabric==1.7'),
                ('Django==1.7', 'Fabric==1.8'),
            )
         )
    )

    assert ret == expected


def test_pin_package_range():

    package = 'Django'
    version_steps = ['1.5', '1.6', '1.7']
    exact = False

    ret = pin_version(package, version_steps, exact)
    expected = ('Django>=1.5,<1.6', 'Django>=1.6,<1.7')
    assert ret == expected


def test_pin_package_exact():

    package = 'Django'
    version_steps = ['1.5', '1.6', '1.7']
    exact = True

    ret = pin_version(package, version_steps, exact)
    expected = ('Django==1.5', 'Django==1.6', 'Django==1.7')
    assert ret == expected
