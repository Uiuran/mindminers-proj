from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='mindminers-proj',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    # version='0.1',
    # according to https://semver.org/
    version='0.2beta',

    description='calculadora para operações na bolsa',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url='http://github.com/Uiuran/mindminers-proj',

    # Author details
    author='Daniel Penalva',
    author_email='dkajah@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords=['data-science'],

    packages=find_packages(),
    install_requires=['numpy', 'scipy','pandas','plotly','jupyter'],
    project_urls={
                 'Documentation':'',
                 #'Funding': 'https://donate.pypi.org',
                 'Source': 'https://github.com/Uiuran/mindminers-proj',
                 'Tracker': ''}
)
