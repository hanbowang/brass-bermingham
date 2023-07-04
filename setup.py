from setuptools import setup, find_packages

setup(
    name='brass',
    version='0.1.0',
    description='Brass Bermingham Playground',
    author='Hanbo Wang',
    url='https://github.com/hanbowang/brass-bermingham',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)