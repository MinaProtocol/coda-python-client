from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

tests_require = ['six', 'pytest', 'pytest-cov', 'python-coveralls', 'mock', 'pysnap']

setup(
    name='CodaClient',
    version='0.0.11',
    python_requires='>=3.5',
    description='A Python wrapper around the Coda Daemon GraphQL API.',
    github='http://github.com/CodaProtocol/coda-python',
    author='Conner Swann',
    author_email='conner@o1labs.org',
    license='Apache License 2.0',
    py_modules=['CodaClient'],
    install_requires=[
        'requests',
        'websockets>=7.0',
        'asyncio'
    ],
    extras_require={
        'test': tests_require,
        'pytest': [
            'pytest',
        ]
    },
    tests_require=tests_require,
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License'
    ],
)