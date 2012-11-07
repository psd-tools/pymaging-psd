#!/usr/bin/env python
from setuptools import setup

setup(
    name = "pymaging-psd",
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://github.com/kmike/pymaging-psd',
    version = '0.6',

    description = 'PSD support for Pymaging',
    license = 'MIT License',
    keywords = "pymaging psd imaging",
    long_description = open('README.rst').read(),

    py_modules = ['pymaging_psd'],
    install_requires = ['psd-tools', 'packbits'],
    entry_points = {'pymaging.formats': ['psd = pymaging_psd:PSD']},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)