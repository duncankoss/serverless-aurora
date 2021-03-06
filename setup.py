#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="serverless-aurora",
    version="0.2.3",
    url='https://github.com/duncankoss/serverless-aurora',
    license='Apache Software License',
    author='dkoss',
    author_email='',
    description='A fork of aurora-data-api',
    long_description=open('README.rst').read(),
    install_requires=[
        'boto3 >= 1.9.245, < 2'
    ],
    extras_require={
    },
    packages=find_packages(exclude=['test']),
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
