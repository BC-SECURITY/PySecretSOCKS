#!/usr/bin/env python
from distutils.core import setup

setup(
    name='PySecretSOCKS',
    version='0.9.1',
    packages=['secretsocks'],
    url='https://github.com/Drewsif/PySecretSOCKS',
    license='MIT',
    author='Drew Bonasera',
    author_email='',
    description='A python SOCKS server for tunneling connections over another channel. Making implementing covert channels a breeze!',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Security'
    ],
    # TODO: This library should be updated to migrate from pyasyncore to asyncio
    # asyncore was deprecated in python 3.6 and removed in python 3.12. This import
    # is a patch to allow this library to be used in python 3.12 and above.
    install_requires=['pyasyncore']
)
