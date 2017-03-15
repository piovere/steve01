#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
    'pytest>=3.0',
]

setup(
    name='steve01',
    version='0.1.0',
    description="Trying to see if I can do Steve's midterm",
    long_description=readme + '\n\n' + history,
    author="J.R. Powers-Luhn",
    author_email='floobyt@gmail.com',
    url='https://github.com/piovere/steve01',
    packages=[
        'steve01',
    ],
    package_dir={'steve01':
                 'steve01'},
    entry_points={
        'console_scripts': [
            'steve01=steve01.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='steve01',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
