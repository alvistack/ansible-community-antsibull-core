# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='antsibull-core',
    version='2.1.0',
    description='Tools for building the Ansible Distribution',
    author_email='Toshio Kuratomi <a.badger@gmail.com>, Felix Fontein <felix@fontein.de>',
    maintainer_email='Felix Fontein <felix@fontein.de>, Maxwell G <maxwell@gtmx.me>',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Ansible',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Typing :: Typed',
    ],
    install_requires=[
        'aiofiles',
        'aiohttp>=3.0.0',
        'build',
        'packaging>=20.0',
        'perky',
        'pydantic<2.0.0,>=1.0.0',
        'pyyaml',
        'semantic-version',
        'sh<2.0.0,>=1.0.0',
        'twiggy>=0.5.0',
    ],
    extras_require={
        'codeqa': [
            'antsibull-changelog',
            'flake8>=6.0.0',
            'pylint>=2.15.7',
            'reuse',
        ],
        'coverage': [
            'coverage[toml]',
        ],
        'dev': [
            'antsibull-core[codeqa]',
            'antsibull-core[coverage]',
            'antsibull-core[formatters]',
            'antsibull-core[test]',
            'antsibull-core[typing]',
            'nox',
        ],
        'formatters': [
            'black',
            'isort',
        ],
        'test': [
            'asynctest',
            'cryptography',
            'pytest',
            'pytest-asyncio>=0.20',
            'pytest-cov',
            'pytest-error-for-skips',
        ],
        'typing': [
            'mypy',
            'pyre-check>=0.9.17',
            'types-aiofiles',
            'types-pyyaml',
        ],
    },
    packages=[
        'antsibull_core',
        'antsibull_core.schemas',
        'antsibull_core.utils',
        'antsibull_core.vendored',
    ],
    package_dir={'': 'src'},
)
