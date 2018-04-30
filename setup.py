from setuptools import setup, find_packages
from codecs import open
from os import path

version = '0.2.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sixfeetup.recipe.runvars',
    description="Buildout recipe to define variables from external commands.",
    long_description=long_description,
    version=version,
    license='BSD',
    py_modules=['sixfeetup.recipe.runvars'],
    packages=find_packages(),
    entry_points={'zc.buildout': ['default=sixfeetup.recipe.runvars:Recipe']},
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    author='Glenn Franxman',
    author_email='glenn@sixfeetup.com',
    url='https://github.com/sixfeetup/sixfeetup.recipe.runvars',
    keywords='runvars recipe',
    classifiers=[
        "Framework :: Buildout",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
