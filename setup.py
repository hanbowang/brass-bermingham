from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()

setup(
    name='brass',
    version='0.1.0',
    description='Brass Bermingham Playground',
    author='Hanbo Wang',
    url='https://github.com/hanbowang/brass-bermingham',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)