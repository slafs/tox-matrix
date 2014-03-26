#!/usr/bin/env python
'''
tox-matrix

Usage:
    tox-matrix generate (-d PACKAGE -v VERSION_STRINGS)... [-p PYVERSION]... [options]
    tox-matrix default

Options:
  generate                    generate tox.ini file with given options
  default                     print default template

  -h --help                   Show this screen.
  --version                   Show version.
  -d PACKAGE, --dep=PACKAGE   Package name as a dependency.

  -v VERSION_STRINGS, --ver=VERSION_STRINGS  Comma seperated list of versions for the given package.

  -p PYVERSION, --pyver=PYVERSION  [default: 2.7 3.3] Python versions for basepython option
                                   (can be given multiple times)

  --template=TEMPLATE          A custom template (full path to a file) to generate a tox.ini file contents.
                               Use `default` to print a default template.

  --exact                      [default: False] Pin exact versions of packages.
'''

from __future__ import print_function
import toxmatrix
from toxmatrix.lib import generate_matrix
from toxmatrix.template import generate_tox_ini
from docopt import docopt
from jinja2 import Environment, FileSystemLoader
import sys
import os


def print_default_template(arguments):
    '''
    just print a default template
    '''
    print(toxmatrix.template.DEFAULT_TEMPLATE, end='')
    return 0


def generate_toxini_contents(arguments):
    '''
    prepare arguments and call `generate_matrix` and `generate_tox_ini`
    '''
    packages = arguments.get('--dep', [])
    version_strings = arguments.get('--ver', [])
    pin_exact = arguments.get('--exact', False)
    py_versions = arguments.get('--pyver', [])
    versions = []
    for ver in version_strings:
        versions.append(ver.split(','))
    matrix = generate_matrix(py_versions, packages, versions, pin_exact)

    template = None
    template_filepath = arguments.get('--template', None)
    if template_filepath is not None:
        directory, filename = os.path.split(template_filepath)
        jinjaenv = Environment(loader=FileSystemLoader(directory or '.'))
        template = jinjaenv.get_template(filename)

    res = generate_tox_ini(matrix, template)
    print(res)
    return 0


def main():
    arguments = docopt(__doc__, version=toxmatrix.__version__)

    print_default = arguments.get('default', False)
    generate_toxini = arguments.get('generate', False)
    ret_code = 0

    if print_default:
        ret_code = print_default_template(arguments)

    if generate_toxini:
        ret_code = generate_toxini_contents(arguments)

    sys.exit(ret_code)

if __name__ == '__main__':
    main()
