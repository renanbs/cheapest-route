from setuptools import setup, find_packages


setup(name='shortest-path',
      description='A Dijkstra implementation',
      long_description='A Dijkstra implementation',
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
              'requests-mock>=1.8.0',
              'pytest-mock>=3.1.1',
          ],
      }
      )
