import os
import unittest

from jsonschema import ValidationError

from rest_tester.function.multiple import MultipleTargetsTestFunctionBuilder
from rest_tester.options import Options
from rest_tester.setting import TestSetting
from test import load_json_data
from test.function import run_test_function_list


class TestMultipleTargetsTestFunctionBuilder(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_post_and_get(self):
        json_file = '%s/resources/test_function_multiple_post_and_get.json' % self.current_dir_path
        test_function_list = self.generate_test_function(json_file)
        run_test_function_list(test_function_list, self)

    def test_put_and_get(self):
        json_file = '%s/resources/test_function_multiple_put_and_get.json' % self.current_dir_path
        test_function_list = self.generate_test_function(json_file)
        run_test_function_list(test_function_list, self)

    def test_put_and_get_unexpected_json_schema(self):
        json_file = '%s/resources/test_function_multiple_put_and_get_unexpected_json_schema.json' % \
                    self.current_dir_path
        test_function_list = self.generate_test_function(json_file)

        with self.assertRaises(ValidationError):
            run_test_function_list(test_function_list, self)

    @staticmethod
    def generate_test_function(json_file):
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data, Options())
        file_name = os.path.basename(json_file)

        builder = MultipleTargetsTestFunctionBuilder(setting, file_name)
        return builder.build()

if __name__ == '__main__':
    unittest.main()
