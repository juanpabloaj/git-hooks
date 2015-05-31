# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="git-hooks",
    version="0.0.1",
    description="Show useful git hooks",
    license="MIT",
    author="JuanPabloAJ",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    package_data={
        'githooks': ['hooks/*']
    },
    entry_points={
        'console_scripts': [
            'git-hooks=githooks:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
