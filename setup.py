from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

tests_require = ['six', 'pytest', 'pytest-cov', 'python-coveralls', 'mock', 'pysnap']

setup(
    name='CodaClient',
    version='0.0.1',
    description='A Python wrapper around the Coda Daemon GraphQL API.',
    github='http://github.com/CodaProtocol/coda-python',
    author='Conner Swann',
    author_email='conner@o1labs.org',
    license='Apache License 2.0',
    py_modules=['CodaClient'],
    install_requires=[
        'requests',
    ],
    extras_require={
        'test': tests_require,
        'pytest': [
            'pytest',
        ]
    },
    tests_require=tests_require,
    long_description=open('README.md').read(),
)