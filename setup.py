import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

version = '0.1.0'

setup(
    name='faker-schema',
    version=version,
    description="Generate fake data using joke2k's faker and your own schema",
    long_description=README,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='faker fixtures data test mock generator schema',
    author='Usman Ehtesham Gul',
    author_email='uehtesham90@gmail.com@gmail.com',
    url='https://github.com/ueg1990/faker-schema',
    license='MIT License',
    packages=find_packages(exclude=["tests"]),
    platforms=["any"],
    test_suite='tests',
    install_requires=[
        "Faker>=0.7.17"
    ]
)