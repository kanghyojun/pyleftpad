from setuptools import setup
from setuptools.config import read_configuration

conf_dict = read_configuration('./setup.cfg')
setup(**conf_dict['options'])
