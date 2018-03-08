from setuptools import setup

setup(
    name='mycustom',
    version='0.1.0',
    py_modules = ['mycustom'],
    entry_points = {"zc.buildout": ["default=mycustom.runvars:Recipe"]},
    )
