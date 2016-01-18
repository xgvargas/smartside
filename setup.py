#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import pkg_resources
import codecs

__version__ = '.'.join( ('0', '1', '7') )


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = [str(req) for req in pkg_resources.parse_requirements(f)]

setup(
    name='smartside',
    version=__version__,
    license="Apache",
    description='Makes PySide a little smarter.',
    long_description=long_description,
    author='Gustavo vargas',
    author_email='xgvargas@gmail.com',
    url='https://github.com/xgvargas/smartside',
    # py_modules = ['smartside'],
    packages = ['smartside'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Build Tools',
    ],
)
