import os
import sys

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'readme.md')).read()
    CHANGES = open(os.path.join(here, 'changes.txt')).read()
except:
    README = ''
    CHANGES = ''

requires = [
    'nive_cms'
]

setupkw = dict(
      name='nive_tmpl_design_json',
      version='0.1',
      description='',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"
      ],
      author='',
      author_email='',
      url='',
      keywords='cms website pyramid',
      license='GPL 3',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="nive_tmpl_design_json",
)

setup(**setupkw)
