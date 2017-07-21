import os
import unittest
import time

from jsonschema import ValidationError

from rest_tester.function.read import ReadTestFunctionBuilder
from rest_tester.setting import TestSetting
from test.helper import load_json_data


class TestReadTestFunctionBuilder(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_build(self):
        json_file = '%s/resources/test_function_read_get.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        self.run_test_function_list(test_function_list, self)

    def test_build_unexpected_status_code(self):
        json_file = '%s/resources/test_function_read_get_unexpected_status_code.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        try:
            self.run_test_function_list(test_function_list, self)
        except AssertionError:
            pass
        else:
            self.fail('Should throw AssertionError!')

    def test_build_unexpected_json_schema(self):
        json_file = '%s/resources/test_function_read_get_unexpected_json_schema.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        try:
            self.run_test_function_list(test_function_list, self)
        except ValidationError:
            pass
        else:
            self.fail('Should throw ValidationError!')

    @staticmethod
    def generate_test_functions(json_file):
        json_data = load_json_data(json_file)
        setting = TestSetting(json_data)

        file_name = os.path.basename(json_file)

        builder = ReadTestFunctionBuilder(setting, file_name)
        return builder.build()

    @staticmethod
    def run_test_function_list(test_function_list, test_self):
        time.sleep(1)

        for test_function in test_function_list:
            test_function.test_function(test_self)

if __name__ == '__main__':
    unittest.main()
