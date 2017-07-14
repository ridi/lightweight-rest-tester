import unittest
import os


from rest_tester.function import TestFunction
from rest_tester.setting import Request


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

        expected_prefix = 'test_%s?' % file_name
        self.assertEqual(actual.find(expected_prefix), 0)

        for key, value in params.items():
            expected_param = '%s=%s' % (key, value)
            self.assertTrue(actual.find(expected_param) >= 0)

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
