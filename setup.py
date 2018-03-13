from setuptools import setup, find_packages

version = '0.2.0'

setup(
    name='sixfeetup.recipe.runvars',
    description="Buildout recipe to define variables from external commands.",
    version=version,
    license='BSD',
    py_modules=['sixfeetup.recipe.runvars'],
    packages=find_packages(),
    entry_points={"zc.buildout": ["default=sixfeetup.recipe.runvars:Recipe"]},
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    author='Glenn Franxman',
    author_email='glenn@sixfeetup.com',
    url='https://github.com/sixfeetup/sfu.recipe.runvars',
    keywords='runvars recipe',
    classifiers=[
        "Framework :: Buildout",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
