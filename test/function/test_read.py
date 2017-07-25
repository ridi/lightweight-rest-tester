import os
import unittest

from jsonschema import ValidationError

from rest_tester.function.read import ReadTestFunctionBuilder
from rest_tester.setting import TestSetting
from test.helper import load_json_data
from . import run_test_function_list


class TestReadTestFunctionBuilder(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_build(self):
        json_file = '%s/resources/test_function_read_get.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        run_test_function_list(test_function_list, self)

    def test_build_unexpected_status_code(self):
        json_file = '%s/resources/test_function_read_get_unexpected_status_code.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        try:
            run_test_function_list(test_function_list, self)
        except AssertionError:
            pass
        else:
            self.fail('Should throw AssertionError!')

    def test_build_unexpected_json_schema(self):
        json_file = '%s/resources/test_function_read_get_unexpected_json_schema.json' % self.current_dir_path
        test_function_list = self.generate_test_functions(json_file)

        try:
            run_test_function_list(test_function_list, self)
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

if __name__ == '__main__':
    unittest.main()
