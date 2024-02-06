#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['typer']

package_data = \
{'': ['*']}

install_requires = \
['click >= 7.1.1, <9.0.0', 'typing-extensions >= 3.7.4.3']

extras_require = \
{'all': ['colorama >=0.4.3,<0.5.0',
         'shellingham >=1.3.0,<2.0.0',
         'rich >=10.11.0,<14.0.0'],
 'dev': ['autoflake >=1.3.1,<2.0.0',
         'flake8 >=3.8.3,<4.0.0',
         'pre-commit >=2.17.0,<3.0.0'],
 'doc': ['mkdocs >=1.1.2,<2.0.0',
         'mkdocs-material >=8.1.4,<9.0.0',
         'mdx-include >=1.4.1,<2.0.0',
         'pillow >=9.3.0,<10.0.0',
         'cairosvg >=2.5.2,<3.0.0'],
 'test': ['shellingham >=1.3.0,<2.0.0',
          'pytest >=4.4.0,<8.0.0',
          'pytest-cov >=2.10.0,<5.0.0',
          'coverage >=6.2,<7.0',
          'pytest-xdist >=1.32.0,<4.0.0',
          'pytest-sugar >=0.9.4,<0.10.0',
          'mypy ==0.971',
          'black >=22.3.0,<23.0.0',
          'isort >=5.0.6,<6.0.0',
          'rich >=10.11.0,<14.0.0']}

setup(name='typer',
      version='0.9.3',
      description='Typer, build great CLIs. Easy to code. Based on Python type hints.',
      author='Sebastián Ramírez',
      author_email='tiangolo@gmail.com',
      url='https://github.com/tiangolo/typer',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.6',
     )
