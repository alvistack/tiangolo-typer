#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['typer']

package_data = \
{'': ['*']}

install_requires = \
['click >= 8.0.0', 'typing-extensions >= 3.7.4.3']

extras_require = \
{'all': ['shellingham >=1.3.0',
         'rich >=10.11.0']}

setup(name='typer',
      version='0.14.0',
      description='Typer, build great CLIs. Easy to code. Based on Python type hints.',
      author='Sebastián Ramírez',
      author_email='tiangolo@gmail.com',
      url='https://github.com/tiangolo/typer',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.7',
     )
