import os
import unittest

from rest_tester.main import generate_test_functions, run_test_functions
from rest_tester.options import Options


class TestsContainer(unittest.TestCase):
    """The test container for dynamically generated test cases."""
    longMessage = True


class TestOptions(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_base_url(self):
        base_url = 'http://localhost:3000'

        options = Options(base_url=base_url)
        self.assertEqual(base_url, options.base_url)

    def test_add_base_url(self):
        base_url = 'http://localhost:3000'
        test_suites_dir = '%s/resources/' % self.current_dir_path

        options = Options(base_url=base_url)

        generate_test_functions(TestsContainer, test_suites_dir, options)
        self.assertTrue(run_test_functions(TestsContainer))

if __name__ == '__main__':
    unittest.main()
