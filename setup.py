from setuptools import setup, find_packages

setup(
    name='empire_earth',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'numpy',
        'matplotlib',
        'pandas',
        'sphinx-autodoc-typehints',
        'pydata-sphinx-theme',
        'jupyter-sphinx',
    ],
    package_data={
        'empire_earth': [
            'databases/*.dat',
            'databases/*.csv',
            'databases/*.txt',
        ],
    },
    include_package_data=True,
    url='https://github.com/byrdie/empire_earth',
    license='',
    author='Roy Smart',
    author_email='roytsmart@gmail.com',
    description='Utilities for calculating unit relationships in the game Empire Earth.'
)
