#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A setuptools based setup module.
"""

import io
import sys
from os import path, system
from shutil import rmtree
from setuptools import find_packages, setup, Command

here = path.abspath(path.dirname(__file__))

# Import the README.rst and use it as the long-description.
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        system('twine upload dist/*')

        sys.exit()


# Where the magic happens:
setup(
    name='pizzapi',
    version='0.0.7',
    description='A Python wrapper for the Dominos Pizza API',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/craigjmidwinter/pizzapi',
    author='craigjmidwinter',
    author_email='craig.j.midwinter@gmail.com',
    keywords='dominos pizza api',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
    install_requires=[
        'pyhamcrest',
        'requests',
        'xmltodict',
    ],
    include_package_data=True,
    python_requires=">=3.6",
    cmdclass={
        'publish': PublishCommand,
    }
)
