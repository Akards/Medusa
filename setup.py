import os
import setuptools
from setuptools import setup

setup(
    name='Medusa',
    version='0.1',
    author='Kinsey McGlasson, Adam Schlossberg, Jimmy Veloso',
    description='A python library of commonly used, parallel algorithms',
    url='https://github.com/Akards/Medusa',
    packages=setuptools.find_packages(exclude=['tests']),
    test_suite='tests',
    python_requires='>3.6',
)
