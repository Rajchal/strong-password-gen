# setup.py
from setuptools import setup, find_packages

setup(
    name='strong_password_generator',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'strong_password_generator=main:main',
        ],
    },
)