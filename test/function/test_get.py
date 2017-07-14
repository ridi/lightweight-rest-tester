import os
import unittest

from jsonschema import ValidationError

from rest_tester.function.get import GetTestFunction
from rest_tester.setting import TestSetting
from test.helper import load_json_data


class TestGetTestFunction(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_make_success(self):
        json_file = '%s/resources/test_function_get_success.json' % self.current_dir_path
        test_function = self.make_get_test_function(json_file)
        test_function(self)

    def test_make_fail_status_code(self):
        json_file = '%s/resources/test_function_get_fail_status_code.json' % self.current_dir_path
        test_function = self.make_get_test_function(json_file)

        try:
            test_function(self)
            self.fail('Should throw AssertionError!')
        except AssertionError:
            pass

    def test_make_fail_json_schema(self):
        json_file = '%s/resources/test_function_get_fail_json_schema.json' % self.current_dir_path
        test_function = self.make_get_test_function(json_file)

        try:
            test_function(self)
            self.fail('Should throw ValidationError!')
        except ValidationError:
            pass

    @staticmethod
    def make_get_test_function(json_file):
        json_data = load_json_data(json_file)
        setting = TestSetting(json_data)

        return GetTestFunction.make(setting.read_request, setting.read_response)

if __name__ == '__main__':
    unittest.main()
