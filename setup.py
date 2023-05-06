# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['antsibull_core',
 'antsibull_core.schemas',
 'antsibull_core.utils',
 'antsibull_core.vendored']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML',
 'aiofiles',
 'aiohttp>=3.0.0',
 'packaging>=20.0',
 'perky',
 'pydantic>=1.0.0,<2.0.0',
 'semantic_version',
 'sh>=1.0.0,<2.0.0',
 'twiggy>=0.5.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 ':python_version >= "3.6" and python_version < "3.7"': ['aiocontextvars']}

setup_kwargs = {
    'name': 'antsibull-core',
    'version': '1.6.0',
    'description': 'Tools for building the Ansible Distribution',
    'author': 'Toshio Kuratomi',
    'author_email': 'a.badger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ansible-community/antsibull-core',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
