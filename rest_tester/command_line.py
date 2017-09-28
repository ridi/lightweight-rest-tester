import unittest

import click
import sys

from rest_tester.main import generate_test_functions, run_test_functions
from rest_tester.options import Options


class TestsContainer(unittest.TestCase):
    pass


@click.command()
@click.argument('test_suites_dir', type=click.Path(exists=True))
@click.option('--base_url', default=None, type=str, help='The base URL of API.')
def main(test_suites_dir, base_url):
    options = Options(base_url=base_url)

    generate_test_functions(TestsContainer, test_suites_dir, options)
    was_successful = run_test_functions(TestsContainer)
    if not was_successful:
        print('Testing was NOT successful!')
        sys.exit(1)
