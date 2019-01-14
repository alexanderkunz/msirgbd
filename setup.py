#!/usr/bin/env python3

import sys
from setuptools import setup


requires = [
    'bottle',
    'noise',
    'psutil'
]
if sys.version_info < (3, 7):
    sys.exit("Python 3.7 or newer is required to run this program.")

setup(
    name='msirgbd',
    python_requires=">3.7",
    description='Daemon for the msi-rgb tool with web interface.',
    long_description='Daemon for the msi-rgb tool with web interface.',
    version='1.0',
    entry_points={
        'console_scripts': ['msirgbd=msirgbd:main'],
    },
    packages=['msirgbd'],
    url='',
    download_url='',
    author='alexanderkunz',
    author_email='',
    install_requires=requires,
)
