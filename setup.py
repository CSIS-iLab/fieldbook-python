#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests>=2.9,<3.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='fieldbook',
    version='0.1.0',
    description="Fieldbook API Client",
    long_description=readme + '\n\n' + history,
    author="Daniel Cloud",
    author_email='daniel@danielcloud.org',
    url='https://github.com/dcloud/fieldbook',
    packages=[
        'fieldbook',
    ],
    package_dir={'fieldbook': 'fieldbook'},
    include_package_data=True,
    install_requires=requirements,
    entry_points={'console_scripts': ['fieldbook = fieldbook.cli:main']},
    license="ISCL",
    zip_safe=False,
    keywords='fieldbook',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
