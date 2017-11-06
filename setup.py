#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'CherryPy',
    'pymongo',
]

setup(
    name='CherryPy-Mongo',
    version='0.1',
    description='Use MongoDB with CherryPy',
    long_description=readme,
    author='Karl Lattimer',
    author_email='karl@qdh.org.uk',
    url='https://github.com/klattimer/cp_mongo',
    packages=[
        'cp_mongo',
    ],
    package_dir={'cp_mongo':
                 'cp_mongo'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='cp_mongo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
