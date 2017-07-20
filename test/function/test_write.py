import os
import unittest

from jsonschema import ValidationError

from rest_tester.function.write import WriteTestFunctionBuilder
from rest_tester.setting import TestSetting
from test.helper import load_json_data


class TestWriteTestFunctionBuilder(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_build_put(self):
        json_file = '%s/resources/test_function_write_put.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)
        test_function.test_function(self)

    def test_build_post(self):
        json_file = '%s/resources/test_function_write_post.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)
        test_function.test_function(self)

    def test_build_put_only(self):
        json_file = '%s/resources/test_function_write_put_only.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)
        test_function.test_function(self)

    def test_build_post_only(self):
        json_file = '%s/resources/test_function_write_post.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)
        test_function.test_function(self)

    def test_build_patch_only(self):
        json_file = '%s/resources/test_function_write_patch_only.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)
        test_function.test_function(self)

    def test_build_delete_only(self):
        json_file = '%s/resources/test_function_write_delete_only.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)
        test_function.test_function(self)

    def test_build_unexpected_status_code(self):
        json_file = '%s/resources/test_function_write_unexpected_status_code.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)

        try:
            test_function.test_function(self)
        except AssertionError:
            pass
        else:
            self.fail('Should throw AssertionError')

    def test_build_unexpected_get(self):
        json_file = '%s/resources/test_function_write_unexpected_get.json' % self.current_dir_path
        test_function = self.generate_test_function(json_file)

        try:
            test_function.test_function(self)
        except ValidationError:
            pass
        else:
            self.fail('Should throw ValidationError')

    @staticmethod
    def generate_test_function(json_file):
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data)
        file_name = os.path.basename(json_file)

        builder = WriteTestFunctionBuilder(setting, file_name)
        return builder.build()

if __name__ == '__main__':
    unittest.main()
