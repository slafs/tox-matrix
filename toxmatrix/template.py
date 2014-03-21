#!/usr/bin/env python
'''
Module for creating tox.ini files
'''
from string import ascii_uppercase
from jinja2 import Template

DEFAULT_TEMPLATE = '''[tox]
envlist = {% for toxenv in envs %}{{ toxenv.name }}{% if not loop.last %}, {% endif %}{% endfor %}

[testenv]
commands = py.test
deps = pytest
{% for toxenv in envs %}
[testenv:{{ toxenv.name }}]
basepython = {{ toxenv.basepython }}
deps = {[testenv]deps}
{%- for dep in toxenv.deps %}
    {{ dep }}
{%- endfor %}
{% endfor %}
'''


def generate_tox_ini(matrix, template=None):
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
    if template is None:
        template = Template(DEFAULT_TEMPLATE)

    for basepython, dep_lists in matrix:
        for deps, suffix in zip(dep_lists, env_suffixes):
            env = tox_env.copy()
            env['basepython'] = basepython
            env['name'] = basepython.replace('thon', '').replace('.', '') + '-' + suffix
            env['deps'] = deps
            envs.append(env)

    rendered = template.render(envs=envs)
    return rendered
