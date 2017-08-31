import unittest
import os


from rest_tester.main import generate_test_functions, run_test_functions
from rest_tester.options import Options


class TestsContainerSuccess(unittest.TestCase):
    """The test container for dynamically generated test cases."""
    longMessage = True


class TestsContainerFail(unittest.TestCase):
    """The test container for dynamically generated test cases."""
    longMessage = True


class TestMain(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_main_success(self):
        test_suites_dir = '%s/resources_success/' % self.current_dir_path

        options = Options(base_url=None)

        generate_test_functions(TestsContainerSuccess, test_suites_dir, options)
        self.assertTrue(run_test_functions(TestsContainerSuccess))

    def test_main_fail(self):
        test_suites_dir = '%s/resources_fail/' % self.current_dir_path

        options = Options(base_url=None)

        generate_test_functions(TestsContainerFail, test_suites_dir, options)
        self.assertFalse(run_test_functions(TestsContainerFail))

if __name__ == '__main__':
    unittest.main()
