from setuptools import setup, find_packages

setup(
    name='plotting_utils',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'seaborn',
        'matplotlib',
        'statannotations',
        'textalloc',
        'joblib'
    ],
)
