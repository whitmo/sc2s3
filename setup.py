from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='sc2s3',
      version=version,
      description="Move files from soundcloud to S3",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='whit',
      author_email='whit@nocoast.us',
      url='http://whitmorriss.org/software/sc2s3',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
