import unittest
import os


from rest_tester.function import TestFunction
from rest_tester.setting import Request
from test.helper import are_equal_lists


class TestTestFunction(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_generate_name(self):
        params = {
            "param_1": "param_1_str",
            "param_2": 2,
            "param_3": "param_3_str",
            "param_4": 4
        }

        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments",
            "params": params
        }

        request = Request(request_data)
        file_name = 'file_name'
        actual = TestFunction.generate_name(file_name, request)

        split_to_url_and_parameters = actual.split('?')
        self.assertEqual(len(split_to_url_and_parameters), 2)

        actual_url = split_to_url_and_parameters[0]
        actual_parameters = split_to_url_and_parameters[1]

        expected_url = 'test_%s' % file_name
        self.assertEqual(actual_url, expected_url)

        actual_parameter_list = actual_parameters.split('&')
        expected_parameter_list = ['%s=%s' % (key, value) for key, value in params.items()]

        self.assertTrue(are_equal_lists(actual_parameter_list, expected_parameter_list))

    def test_generate_name_no_param(self):
        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments",
            "params": {}
        }

        file_name = 'file_name'
        request = Request(request_data)

        actual = TestFunction.generate_name(file_name, request)
        expected = 'test_%s' % file_name

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
