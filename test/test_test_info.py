import unittest
import json
import os

from rest_tester.test_info import TestInfo


class TestTestInfo(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_read_all(self):
        json_file = '%s/resources/test_info_success_all.json' % self.current_dir_path
        json_data = self.load_json_data(json_file)

        url, params, timeout, test_cases = TestInfo.read(json_data)

        self.assertEqual(json_data['api']['url'], url)
        self.assertEqual(json_data['api']['params'], params)
        self.assertEqual(json_data['api']['timeout'], timeout)
        self.assertEqual(json_data['tests'], test_cases)

    def test_read_partial(self):
        json_file = '%s/resources/test_info_success_partial.json' % self.current_dir_path
        json_data = self.load_json_data(json_file)

        url, params, timeout, test_cases = TestInfo.read(json_data)

        self.assertEqual(json_data['api']['url'], url)
        self.assertEqual(json_data['tests'], test_cases)

    def test_read_fail_missing_url(self):
        json_file = '%s/resources/test_info_fail_missing_url.json' % self.current_dir_path
        json_data = self.load_json_data(json_file)

        self.run_fail_function(json_data, KeyError)

    def test_read_fail_missing_tests(self):
        json_file = '%s/resources/test_info_fail_missing_tests.json' % self.current_dir_path
        json_data = self.load_json_data(json_file)

        self.run_fail_function(json_data, KeyError)

    @staticmethod
    def load_json_data(json_file):
        with open(json_file, 'r') as json_file:
            return json.load(json_file)

    def run_fail_function(self, json_data, error):
        """Helper function for unsuccessful run; should throw given error."""
        try:
            TestInfo.read(json_data)
            self.fail('Should throw AssertionError!')
        except error:
            pass
