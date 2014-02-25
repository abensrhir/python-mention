from setuptools import setup, find_packages

requires_list = [
  'argparse>=1.2.1',
  'rauth>=0.5.5',
  'requests>=1.2.3',

setup(name='mentionpy',
      version='1.04b',
      platforms='any',
      description='Python library for Mention App',
      author='Anass Bensrhir',
      author_email='abensrhir@gmail.com',
      url='https://github.com/abensrhir/python-mention',
      packages = ['mentionpy'],
      include_package_data=True,
      install_requires=requires_list,
      classifiers = [
        'Programming Language :: Python :: 2.7',
      ]
)
