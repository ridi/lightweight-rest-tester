from setuptools import setup, find_packages

setup(name='lightweight-rest-tester',
      version='1.2.0',
      description='A lightweight REST API testing framework.',
      url='https://github.com/ridibooks/lightweight-rest-tester',
      author='Jeehoon Yoo',
      author_email='jeehoon.yoo@ridi.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'lw_rest_tester = rest_tester.command_line:main'
          ],
      })
