import setuptools
from setuptools import setup

with open('README.md') as fh:
    long_description = fh.read()


setup(
    name='BulkSmsZim',
    version='1.2.1',
    author='Marlvin Chihota',
    author_email='info@marlvinzw.me',
    description='A Helper Library For Sending Text Messages For BulkSmsZimApi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MarlvinzW/BulkSmsZim-Api',
    download_url='https://github.com/MarlvinzW/BulkSmsZim-Api',
    install_requires=['requests'],
    py_modules=['BulkSmsZimApi'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
