from setuptools import setup, find_packages

setup(name='lightweight-rest-tester',
      version='1.5.0',
      description='A lightweight REST API testing framework.',
      url='https://github.com/ridibooks/lightweight-rest-tester',
      author='Jeehoon Yoo',
      author_email='jeehoon.yoo@ridi.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'certifi==2017.4.17',
          'chardet==3.0.4',
          'idna==2.5',
          'jsonschema==2.6.0',
          'requests==2.18.1',
          'urllib3==1.21.1',
          'click==6.7',
      ],
      entry_points={
          'console_scripts': [
              'lw_rest_tester = rest_tester.command_line:main'
          ],
      })
