#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_template
----------------------------------

Tests for `toxmatrix.template` module.
"""

from toxmatrix.template import generate_tox_ini, DEFAULT_TEMPLATE
from jinja2 import Template


def test_default_template():

    matrix = (
        ('python2.7',
            (
                ('Django>=1.5,<1.6', 'Fabric>=1.5,<1.6'),
                ('Django>=1.6,<1.7', 'Fabric>=1.5,<1.6'),
            )
         ),
        ('python3.3',
            (
                ('Django>=1.5,<1.6', 'Fabric>=1.5,<1.6'),
                ('Django>=1.6,<1.7', 'Fabric>=1.5,<1.6'),
            )
         )
    )

    tpl = Template(DEFAULT_TEMPLATE)

    expected = '''[tox]
envlist = py27-A,py27-B,py33-A,py33-B,

[testenv]
commands = py.test

[testenv:py27-A]
basepython = python2.7
deps = {[testenv]deps}
    Django>=1.5,<1.6
    Fabric>=1.5,<1.6

[testenv:py27-B]
basepython = python2.7
deps = {[testenv]deps}
    Django>=1.6,<1.7
    Fabric>=1.5,<1.6

[testenv:py33-A]
basepython = python3.3
deps = {[testenv]deps}
    Django>=1.5,<1.6
    Fabric>=1.5,<1.6

[testenv:py33-B]
basepython = python3.3
deps = {[testenv]deps}
    Django>=1.6,<1.7
    Fabric>=1.5,<1.6
'''

    ret = generate_tox_ini(matrix, tpl)

    assert ret == expected
