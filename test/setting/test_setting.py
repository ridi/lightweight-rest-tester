import os
import unittest


from rest_tester.setting import TestSetting, TestMethod, SettingMethodError, SettingIncompleteInformationError
from test import helper


class TestTestSetting(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_get(self):
        json_file = '%s/resources/test_setting_get.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertEqual(
                json_data[TestMethod.GET][TestSetting.KEY_API],
                self.convert_api_to_dict(setting.read_api)
        )
        self.assertEqual(
                json_data[TestMethod.GET][TestSetting.KEY_TESTS],
                self.convert_tests_to_dict(setting.read_tests)
        )

    def test_get_missing_response(self):
        json_file = '%s/resources/test_setting_get_missing_response.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        try:
            TestSetting(json_data)
        except SettingIncompleteInformationError:
            pass
        else:
            self.fail('Should throw KeyError!')

    def test_post(self):
        json_file = '%s/resources/test_setting_post.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertEqual(
                json_data[TestMethod.POST][TestSetting.KEY_API],
                self.convert_api_to_dict(setting.write_api)
        )
        self.assertEqual(
                json_data[TestMethod.POST][TestSetting.KEY_TESTS],
                self.convert_tests_to_dict(setting.write_tests)
        )

        self.assertEqual(
                json_data[TestMethod.GET][TestSetting.KEY_API],
                self.convert_api_to_dict(setting.read_api)
        )
        self.assertEqual(
                json_data[TestMethod.GET][TestSetting.KEY_TESTS],
                self.convert_tests_to_dict(setting.read_tests)
        )

    def test_post_only(self):
        json_file = '%s/resources/test_setting_post_only.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertEqual(
                json_data[TestMethod.POST][TestSetting.KEY_API],
                self.convert_api_to_dict(setting.write_api)
        )
        self.assertEqual(
                json_data[TestMethod.POST][TestSetting.KEY_TESTS],
                self.convert_tests_to_dict(setting.write_tests)
        )

    def test_post_missing_response(self):
        json_file = '%s/resources/test_setting_post_missing_response.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        try:
            TestSetting(json_data)
        except SettingIncompleteInformationError:
            pass
        else:
            self.fail('Should throw KeyError!')

    @staticmethod
    def convert_api_to_dict(api):
        api_dict = {}
        if api.data:
            api_dict[api.KEY_DATA] = api.data
        if api.params:
            api_dict[api.KEY_PARAMS] = api.params
        if api.url:
            api_dict[api.KEY_URL] = api.url

        return api_dict

    @staticmethod
    def convert_tests_to_dict(tests):
        tests_dict = {}
        if tests.timeout:
            tests_dict[tests.KEY_TIMEOUT] = tests.timeout
        if tests.status_code:
            tests_dict[tests.KEY_STATUS_CODE] = tests.status_code
        if tests.json_schema:
            tests_dict[tests.KEY_JSON_SCHEMA] = tests.json_schema

        return tests_dict


if __name__ == '__main__':
    unittest.main()
