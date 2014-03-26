#!/usr/bin/env python
'''
Module for generic helpers
'''
from itertools import product


def pin_version(package_name, version_steps, exact=False):
    '''
    create a tuple of strings with package and pinned versions.

    :param package_name: package name to be pinned
    :param version_steps: an iterable of versions for the given package name
    :param exact: same as in `generate_matrix`
    '''

    exact_format = '{0}=={1}'
    nonexact_format = '{0}>={1},<{2}'
    ret = []

    if exact:
        for version_string in version_steps:
            ret.append(exact_format.format(package_name, version_string))
    else:
        current = None
        previous = None

        for version_string in version_steps:
            current = version_string
            if previous is not None:
                ret.append(nonexact_format.format(package_name, previous, current))

            previous = current

    return tuple(ret)


def generate_matrix(python_versions, packages, version_steps, pin_exact=False):
    '''
    returns a matrix of packages and its versions including different python
    versions

    :param python_versions: iterable of python version strings e.g. ('2.7', '3.3')

    :param packages: iterable of package names e.g. ('Django', 'Fabric')

    :param version_steps:
        iterable of iterables of version strings from above packages
        e.g. (('1.5', '1.6', '1.7'), ('1.6', '1.7', '1.8'))

    :param pin_exact:
        defines whether to pin exactly above version.

        if *True* then use exact specified versions
        (e.g. to produce something like ('Django==1.5', 'Django==1.6', 'Django==1.7'))

        if *False* then use specified versions as boundaries
        (e.g. to produce something like ('Django>=1.5,<1.6', 'Django>=1.6,<1.7')

    :return list:

        an iterable of two tuples e.g.::

            [('python2.7', (
                ('Django>=1.5,<1.6', 'Fabric>=1.6,<1.7'),
                ('Django>=1.5,<1.6', 'Fabric>=1.7,<1.8'),
                ('Django>=1.6,<1.7', 'Fabric>=1.6,<1.7'),
                ('Django>=1.6,<1.7', 'Fabric>=1.7,<1.8'),
                )
              ),
             ('python3.3', (
                ('Django>=1.5,<1.6', 'Fabric>=1.6,<1.7'),
                ('Django>=1.5,<1.6', 'Fabric>=1.7,<1.8'),
                ('Django>=1.6,<1.7', 'Fabric>=1.6,<1.7'),
                ('Django>=1.6,<1.7', 'Fabric>=1.7,<1.8'),
                )
              ),
            ]

    '''
    ret = []

    dependencies = []
    for package, versions in zip(packages, version_steps):

        package_deps = pin_version(package, versions, pin_exact)
        dependencies.append(package_deps)

    gen = product(*dependencies)
    deps_for_py = tuple(gen)

    for pyver in python_versions:
        semi_deps = tuple(['python{0}'.format(pyver), deps_for_py])
        ret.append(semi_deps)

    return tuple(ret)
