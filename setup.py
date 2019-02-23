# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

__description__ = 'Api REST Python Flask'
__long_description__ = 'This is an api for SW Universe B2W chalenge'

__author__ = 'Anderson Picollo'
__author_email__ = 'andersonpicollo@gmail.com'

testing_extras = [
    'pytest',
    'pytest-cov',
]


setup(
    name='swdesafio',
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/andersonpicollo/swdesafio',
    keywords='API, REST, Flask, MongoDB',
    include_package_data=True,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)