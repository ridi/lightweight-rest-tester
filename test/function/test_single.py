import os
import unittest

from requests.exceptions import ConnectTimeout
from jsonschema import ValidationError

from rest_tester.function.single import SingleTargetTestFunctionBuilder
from rest_tester.setting import TestSetting
from test import load_json_data
from test.function import run_test_function_list


class TestSingleTargetTestFunctionBuilder(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_get(self):
        json_file = '%s/resources/test_function_single_get.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)
        run_test_function_list(test_function_list, self)

    def test_get_unexpected_timeout(self):
        json_file = '%s/resources/test_function_single_get_unexpected_timeout.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        with self.assertRaises(ConnectTimeout):
            run_test_function_list(test_function_list, self)

    def test_get_unexpected_status_code(self):
        json_file = '%s/resources/test_function_single_get_unexpected_status_code.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        with self.assertRaises(AssertionError):
            run_test_function_list(test_function_list, self)

    def test_get_unexpected_json_schema(self):
        json_file = '%s/resources/test_function_single_get_unexpected_json_schema.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        with self.assertRaises(ValidationError):
            run_test_function_list(test_function_list, self)

    def test_delete(self):
        json_file = '%s/resources/test_function_single_delete.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)
        run_test_function_list(test_function_list, self)

    def test_patch(self):
        json_file = '%s/resources/test_function_single_patch.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)
        run_test_function_list(test_function_list, self)

    def test_post(self):
        json_file = '%s/resources/test_function_single_post.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)
        run_test_function_list(test_function_list, self)

    def test_put(self):
        json_file = '%s/resources/test_function_single_put.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)
        run_test_function_list(test_function_list, self)

    def test_put_multi_params(self):
        json_file = '%s/resources/test_function_single_put_multi_params.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)
        run_test_function_list(test_function_list, self)

    def test_put_unexpected_status_code(self):
        json_file = '%s/resources/test_function_single_put_unexpected_status_code.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        with self.assertRaises(AssertionError):
            run_test_function_list(test_function_list, self)

    @staticmethod
    def generate_test_functions(json_file):
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data)
        file_name = os.path.basename(json_file)

        builder = SingleTargetTestFunctionBuilder(setting, file_name)
        return builder.build()

if __name__ == '__main__':
    unittest.main()
