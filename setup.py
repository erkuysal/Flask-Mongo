from distutils.core import setup
from setuptools import find_packages
import os


# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Name of the package
    # name=<name of current directory>,
    name='Development/Python/Web/project_foxtrot',


    # Packages to include into the distribution
    packages=find_packages('.'),

    # Start with a small number and increase it with every change you make
    # https://semver.org
    version='1.0.0',

    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    # For example: MIT
    license='',

    # Short description of your library
    description='',

    # Long description of your library
    long_description=long_description,
    long_description_context_type='text/markdown',

    # Your name
    author='Feyzullah Uysal, Talha Yildirim, Emir Aydin',

    # Your email
    author_email='f.erkuysal@gmail.com',

    # Either the link to your github or to your website
    url='https://github.com/erkuysal/Flask-Mongo',

    # Link from which the project can be downloaded
    download_url='',

    # List of keyword arguments
    keywords=[],

    # List of packages to install with this one
    install_requires=['python == 3.12',
                      'flask == 3.0.0',
                      'flask-bootstrap == 3.3.7.1',
                      'bootstrap-flask == 2.3.3',
                      'flask-login == 0.6.3',
                      'flask-mongoengine == 1.0.1',
                      'bcrypt ==  4.1.2'],

    # https://pypi.org/classifiers/
    classifiers=[]
)
