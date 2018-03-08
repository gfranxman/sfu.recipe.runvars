from setuptools import setup

setup(
    name='sfu.recipe.runvars',
    version='0.1.0',
    py_modules = ['sfu.recipe.runvars'],
    packages= [ 'sfu', 'sfu.recipe', 'sfu.recipe.runvars'],
    entry_points = {"zc.buildout": ["default=sfu.recipe.runvars:Recipe"]},
    )
