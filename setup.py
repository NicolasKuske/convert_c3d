from os import path
from setuptools import setup

script_dir = 'scripts'

setup(name='c3d_repair',
      version='0.2',
      description='Scripts for rewriting c3d files to be compatible with various acquisition and analysis systems.',
      scripts=[path.join(script_dir, 'convert_c3d.py')],
      requires=['btk']
      )

