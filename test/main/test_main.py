import unittest
import os


from rest_tester.main import generate_test_functions, run_test_functions
from rest_tester.options import Options


class TestMain(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_main(self):
        test_suites_dir = '%s/resources/' % self.current_dir_path

        options = Options(base_url=None)

        generate_test_functions(test_suites_dir, options)
        run_test_functions()

if __name__ == '__main__':
    unittest.main()
