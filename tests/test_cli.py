#!/usr/bin/env python

from toxmatrix.cli import print_default_template
from toxmatrix.template import DEFAULT_TEMPLATE


def test_default(capfd):
    # use a pytest fixture here
    arguments = {}
    print_default_template(arguments)

    resout, reserr = capfd.readouterr()

    assert reserr == ''

    assert resout == DEFAULT_TEMPLATE
