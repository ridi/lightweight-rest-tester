import unittest
import json
import os

from jsonschema import ValidationError

from rest_tester.test_function import TestFunction
from rest_tester.test_info import TestInfo


class TestTestFunction(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_generate_name_with_no_params(self):
        file_name = 'file_name'
        test_key = 'test_key'
        params = {}

        actual = TestFunction.generate_name(file_name, test_key, params)
        expected = 'test_%s_%s' % (file_name, test_key)

        self.assertEqual(actual, expected)

    def test_generate_name_with_params(self):
        file_name = 'file_name'
        test_key = 'test_key'
        params = {
            'param_1': 'param_1_str',
            'param_2': 2,
            'param_3': 'param_3_str',
            'param_4': 4
        }

        actual = TestFunction.generate_name(file_name, test_key, params)

        expected_prefix = 'test_%s_%s?' % (file_name, test_key)
        self.assertEqual(actual.find(expected_prefix), 0)

        for key, value in params.items():
            expected_param = '%s=%s' % (key, value)
            self.assertTrue(actual.find(expected_param) >= 0)

    def test_make_test_status_code(self):
        json_file = '%s/resources/status_code_success.json' % self.current_dir_path
        url, params, timeout, test_cases = self.load_test_info(json_file)

        test_key = 'statusCode'

        self.run_success_function(url, params, timeout, test_key, test_cases[test_key])

    def test_make_test_status_code_fail(self):
        json_file = '%s/resources/status_code_fail.json' % self.current_dir_path
        url, params, timeout, test_cases = self.load_test_info(json_file)

        test_key = 'statusCode'

        self.run_fail_function(url, params, timeout, test_key, test_cases[test_key], AssertionError)

    def test_make_test_json_schema(self):
        json_file = '%s/resources/json_schema_success.json' % self.current_dir_path
        url, params, timeout, test_cases = self.load_test_info(json_file)

        test_key = 'jsonSchema'

        self.run_success_function(url, params, timeout, test_key, test_cases[test_key])

    def test_make_test_json_schema_fail(self):
        json_file = '%s/resources/json_schema_fail.json' % self.current_dir_path
        url, params, timeout, test_cases = self.load_test_info(json_file)

        test_key = 'jsonSchema'

        self.run_fail_function(url, params, timeout, test_key, test_cases[test_key], ValidationError)

    def test_make_test_unsupported_case(self):
        json_file = '%s/resources/unsupported_case.json' % self.current_dir_path
        url, params, timeout, test_cases = self.load_test_info(json_file)

        test_key = 'unsupportedCase'

        self.run_fail_function(url, params, timeout, test_key, test_cases[test_key], AssertionError)

    def run_success_function(self, url, params, timeout, test_key, test_case):
        """Helper function for successful run."""
        test_function = TestFunction.make(url, params, timeout, test_key, test_case)
        test_function(self)

    def run_fail_function(self, url, params, timeout, test_key, test_case, error):
        """Helper function for unsuccessful run; should throw given error."""
        test_function = TestFunction.make(url, params, timeout, test_key, test_case)
        try:
            test_function(self)
            self.fail('Should throw AssertionError!')
        except error:
            pass

    @staticmethod
    def load_test_info(json_file):
        """Load test information from JSON file."""
        with open(json_file, 'r') as json_file:
            json_data = json.load(json_file)
            return TestInfo.read(json_data)
