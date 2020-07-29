from setuptools import setup, find_packages


setup(name='shortest-path',
      description='A basic Dijkstra implementation',
      long_description='A basic Dijkstra implementation, that use a REST API and a command line.'
                       'The project is organized following a Domain Driven Design approach.',
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version='1.0.0',
      install_requires=[
          'wheel==0.34.2',
          'flask==1.1.2',
      ],
      extras_require={
          'dev': [
              'pytest>=5.4.3',
              'pytest-mock>=3.1.1',
              'pytest-lazy-fixture>=0.6.3',
          ],
      }
      )
