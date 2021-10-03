# -*- coding: utf-8 -*-
"""
Mais, a python package for predicting Major League Soccer.
"""

import io
from setuptools import find_packages, setup


with io.open('LICENSE') as f:
    license = f.read()


setup(
    name='mais',
    version='0.9.1',
    description='Predict games in Major League Soccer',
    url='https://github.com/matt-bernhardt/mais',
    license=license,
    author='Matt Bernhardt',
    author_email='matt.j.bernhardt@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'xlrd',
        'numpy',
        'mysql-connector-python-rf',
    ],
    dependency_links=[
        'http://dev.mysql.com/downloads/connector/python/',
    ],
    entry_points={
        'console_scripts': ['mais=mais.command_line:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intendend Audience :: Other Audience',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ]
)
