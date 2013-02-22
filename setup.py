import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'mako',
    'requests',
    'wtforms'
    ]

setup(name='hawkeye',
      version='0.1',
      description='python nokkhum client',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: hawkeye",
        ],
      author='Attasuntorn Traisuwan  Yoschanin Sasiwat, Wongpiti Wangsanti, Thanathip Limna',
      author_email='',
      maintainer="Thanathip Limna",
      license = 'xxx License',
      packages = find_packages(),
      url='https://github.com/sdayu/python-nokkhumclient',
      keywords='VSaaS, python client',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
#      tests_require=requires,
#      test_suite="nokkhum-controller",
      )

