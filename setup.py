from setuptools import setup, find_packages

setup(
    name='empire_earth',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'numpy',
        'pandas',
        'sphinx-autodoc-typehints',
        'astropy-sphinx-theme',
        'jupyter-sphinx',
    ],
    package_data={
        'empire_earth': [
            'empire_earth/databases/*.dat',
            'empire_earth/databases/*.csv',
            'empire_earth/databases/*.txt',
        ],
    },
    include_package_data=True,
    url='https://github.com/byrdie/empire_earth',
    license='',
    author='Roy Smart',
    author_email='roytsmart@gmail.com',
    description='Utilities for calculating unit relationships in the game Empire Earth.'
)
