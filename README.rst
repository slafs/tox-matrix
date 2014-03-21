===============================
Tox Matrix
===============================

.. image:: https://badge.fury.io/py/tox-matrix.png
    :target: http://badge.fury.io/py/tox-matrix

.. image:: https://travis-ci.org/slafs/tox-matrix.png?branch=master
        :target: https://travis-ci.org/slafs/tox-matrix

.. image:: https://pypip.in/d/tox-matrix/badge.png
        :target: https://crate.io/packages/tox-matrix?version=latest


Project for creating tox.ini files with multiple dependencies.

* Free software: BSD license
* Documentation: http://tox-matrix.rtfd.org.

A little utility script to generate ``tox.ini`` files.
It should be handy in case where your project have multiple different dependencies
with different version and you would like to test all available configurations of them.


Quick start
--------------

Install it::

    pip install tox-matrix


Now let's assume you'd like to test your project against different versions
of ``Django`` (latest 1.5.X and 1.6.X ) and ``Fabric`` (latest 1.7.X and 1.8.X)
using ``python2.7`` and ``python3.3``.
You could do something like this::

    tox-matrix generate -d Django -v 1.5,1.6,1.7 -d Fabric -v 1.7,1.8,1.9 -p 2.7 -p 3.3

Which should generate this ``tox.ini`` file content to stdout::

    [tox]
    envlist = py27-A, py27-B, py27-C, py27-D, py33-A, py33-B, py33-C, py33-D

    [testenv]
    commands = py.test

    [testenv:py27-A]
    basepython = python2.7
    deps = {[testenv]deps}
        Django>=1.5,<1.6
        Fabric>=1.7,<1.8

    [testenv:py27-B]
    basepython = python2.7
    deps = {[testenv]deps}
        Django>=1.5,<1.6
        Fabric>=1.8,<1.9

    [testenv:py27-C]
    basepython = python2.7
    deps = {[testenv]deps}
        Django>=1.6,<1.7
        Fabric>=1.7,<1.8

    [testenv:py27-D]
    basepython = python2.7
    deps = {[testenv]deps}
        Django>=1.6,<1.7
        Fabric>=1.8,<1.9

    [testenv:py33-A]
    basepython = python3.3
    deps = {[testenv]deps}
        Django>=1.5,<1.6
        Fabric>=1.7,<1.8

    [testenv:py33-B]
    basepython = python3.3
    deps = {[testenv]deps}
        Django>=1.5,<1.6
        Fabric>=1.8,<1.9

    [testenv:py33-C]
    basepython = python3.3
    deps = {[testenv]deps}
        Django>=1.6,<1.7
        Fabric>=1.7,<1.8

    [testenv:py33-D]
    basepython = python3.3
    deps = {[testenv]deps}
        Django>=1.6,<1.7
        Fabric>=1.8,<1.9


Features
--------

* Generate tox.ini files
* Pin versions either with exact ones or by range
* Use a Jinja2 template for your tox.ini file
