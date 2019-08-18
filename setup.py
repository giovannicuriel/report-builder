# -*- coding: utf-8 -*-
"""
setup.py script
"""

import io
from collections import OrderedDict
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    README = f.read()

setup(
    name='reportbuilder',
    version='0.0.1',
    url='http://github.com/giovannicuriel/report-builder',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/giovannicuriel/report-builder.git'),
        ('Issue tracker', 'https://github.com/giovannicuriel/report-builder/issues'),
    )),
    license='BSD-2-Clause',
    author='Giovanni Curiel dos Santos',
    author_email='giovannicuriel@gmail.com',
    description='Sample package for Python training courses',
    long_description=README,
    packages=["reportbuilder"],
    include_package_data=True,
    zip_safe=False,
    platforms=[any],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'flask==1.1.1'
    ],
    entry_points={
        'console_scripts': [
            'report-builder = reportbuilder.app:main'
        ]
    }
)
