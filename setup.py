from setuptools import setup
from setuptools import find_packages
import sys 
import os

version = '0.0'

requires = ['cliff',
            'cliff-tablib',
            'requests',
            'boto']

setup(name='sc2s3',
      version=version,
      description="Move files from soundcloud to S3",
      long_description=""" """,
      classifiers=[], 
      keywords='',
      author='whit',
      author_email='whit at nocoast.us',
      url='http://whitmorriss.org/software/sc2s3',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      [console_scripts]
      sc2s3=sc2s3.cli:main

      [sc2s3.cli]
      urls=c2s3.cli:SCUrls
      """,
      )

