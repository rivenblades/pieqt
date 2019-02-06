# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pieqt',
    version='0.0.1',
    description='simple description',
    long_description=readme,
    author='kostas_petsis',
    author_email='kostaspetsis@outlook.com',
    url='project_url',
    license=license,
    packages=find_packages(),
)
