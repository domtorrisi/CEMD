# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cemd',
    version='0.0.1',
    description='Customer Energy Management Device',
    long_description=readme,
    author='Dominic Torrisi',
    author_email='domtorrisi93@gmail.com',
    url='https://github.com/domtorrisi/CEMD',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
