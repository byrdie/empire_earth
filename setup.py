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
    include_package_data=True,
    url='https://github.com/byrdie/empire_earth',
    license='',
    author='Roy Smart',
    author_email='roytsmart@gmail.com',
    description='Utilities for calculating unit relationships in the game Empire Earth.'
)
