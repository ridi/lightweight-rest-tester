import os
import unittest

from rest_tester.main import generate_test_functions, run_test_functions
from rest_tester.options import Options, AuthenticationError


class TestsContainer(unittest.TestCase):
    pass


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

    def test_auth(self):
        user = 'user'
        password = 'pass'

        options = Options(auth=user + ':' + password)

        expected = (user, password)

        self.assertEqual(expected, options.auth)

    def test_read_authentication(self):
        user = 'user'
        password = 'pass'

        actual = Options._read_authentication(user + ':' + password)
        expected = (user, password)

        self.assertEqual(expected, actual)

    def test_read_authentication_fail(self):
        user = 'user'
        password = 'pass'

        with self.assertRaises(AuthenticationError):
            Options._read_authentication(user + password)

    def test_insecure(self):
        insecure = True
        options = Options(insecure=insecure)

        expected = insecure

        self.assertEqual(expected, options.insecure)

    def test_insecure_default(self):
        options = Options()

        self.assertFalse(options.insecure)

if __name__ == '__main__':
    unittest.main()
