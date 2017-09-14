with open('setup.py') as fobj:
    for line in fobj:
        print line,
#!/usr/bin/env python
"""Factorial project"""
from setuptools import find_packages, setup
setup(name = 'factorial',
    version = '0.1',
    description = "Factorial module.",
    long_description = "A test module for our book.",
    platforms = ["Linux"],
    author="Kushal Das",