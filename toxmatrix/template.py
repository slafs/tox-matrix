#!/usr/bin/env python
'''
Module for creating tox.ini files
'''
from string import ascii_uppercase

DEFAULT_TEMPLATE = '''[tox]
envlist = {% for toxenv in envs %}{{ toxenv.name }},{% endfor %}

[testenv]
commands = py.test
{% for toxenv in envs %}
[testenv:{{ toxenv.name }}]
basepython = {{ toxenv.basepython }}
deps = {[testenv]deps}{%- for dep in toxenv.deps  %}
    {{ dep }}
{%- endfor %}
{% endfor %}
'''


def generate_tox_ini(matrix, template):
    '''
    Generate a tox.ini file contents from a given matrix using a template

    :param matrix: as returned from `toxmatrix.lib.generate_matrix`
    :param template: a template to render tox.ini with Jinja2
    '''

    tox_env = {
        'name': None,
        'basepython': None,
        'deps': [],
    }

    envs = []
    env_suffixes = ascii_uppercase

    for basepython, dep_lists in matrix:
        for deps, suffix in zip(dep_lists, env_suffixes):
            env = tox_env.copy()
            env['basepython'] = basepython
            env['name'] = basepython.replace('thon', '').replace('.', '') + '-' + suffix
            env['deps'] = deps
            envs.append(env)

    rendered = template.render(envs=envs)
    return rendered
