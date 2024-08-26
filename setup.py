from setuptools import setup, find_packages

setup(
    name='Clog',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'colorama>=0.4.4',
    ],
    description='Custom logger with colored console output',
    author='BITIW',
    author_email='admin@ourmcc.world',
)
