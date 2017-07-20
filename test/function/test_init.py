import unittest
import os


from rest_tester.function import TestFunctionBuilderFactory, TestFunctionBuilder
from rest_tester.function.read import ReadTestFunctionBuilder
from rest_tester.function.write import WriteTestFunctionBuilder
from rest_tester.setting import Request, TestSetting
from test.helper import are_equal_lists, load_json_data


class TestTestFunction(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_get_read(self):
        json_file = '%s/resources/test_function_init_get_read.json' % self.current_dir_path
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data)
        file_name = os.path.basename(json_file)

        builder = TestFunctionBuilderFactory.get_builder(setting, file_name)
        self.assertTrue(isinstance(builder, ReadTestFunctionBuilder))

    def test_get_write(self):
        json_file = '%s/resources/test_function_init_get_write.json' % self.current_dir_path
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data)
        file_name = os.path.basename(json_file)

        builder = TestFunctionBuilderFactory.get_builder(setting, file_name)
        self.assertTrue(isinstance(builder, WriteTestFunctionBuilder))

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
        actual = TestFunctionBuilder._generate_name(file_name, request)

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

        actual = TestFunctionBuilder._generate_name(file_name, request)
        expected = 'test_%s' % file_name

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
