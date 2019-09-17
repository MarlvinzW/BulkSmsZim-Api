import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='BulkSmsZim',
    version='1.0',
    scripts=['BulkSmsZim'],
    author='Marlvin Chihota',
    author_email='info@marlvinzw.me',
    description='A Helper Library For Sending Text Messages For BulkSmsZim',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MarlvinzW/BulkSmsZim-Api',
    download_url='https://github.com/MarlvinzW/BulkSmsZim-Api',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independant',
    ]
)
