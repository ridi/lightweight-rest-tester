import os
import unittest


from rest_tester.setting import TestSetting
from test import helper


class TestTestSetting(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_get_success(self):
        json_file = '%s/resources/test_setting_get_success.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertEqual(json_data['get']['request'], self.convert_request_to_dict(setting.read_request))
        self.assertEqual(json_data['get']['response'], self.convert_response_to_dict(setting.read_response))

    def test_get_fail_all(self):
        json_file = '%s/resources/test_setting_get_fail_all.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        try:
            setting = TestSetting(json_data)
            self.fail('Should throw KeyError!')
        except KeyError:
            pass

    def test_get_fail_partial(self):
        json_file = '%s/resources/test_setting_get_fail_partial.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        try:
            setting = TestSetting(json_data)
            self.fail('Should throw KeyError!')
        except KeyError:
            pass

    def test_post_success(self):
        json_file = '%s/resources/test_setting_post_success.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertEqual(json_data['post']['request'], self.convert_request_to_dict(setting.write_request))
        self.assertEqual(json_data['post']['response'], self.convert_response_to_dict(setting.write_response))

        self.assertEqual(json_data['get']['request'], self.convert_request_to_dict(setting.read_request))
        self.assertEqual(json_data['get']['response'], self.convert_response_to_dict(setting.read_response))

    def test_post_success_no_get(self):
        json_file = '%s/resources/test_setting_post_success_no_get.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertEqual(json_data['post']['request'], self.convert_request_to_dict(setting.write_request))
        self.assertEqual(json_data['post']['response'], self.convert_response_to_dict(setting.write_response))

    def test_post_fail_all(self):
        json_file = '%s/resources/test_setting_post_fail_all.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        try:
            setting = TestSetting(json_data)
            self.fail('Should throw KeyError!')
        except KeyError:
            pass

    def test_post_fail_partial(self):
        json_file = '%s/resources/test_setting_post_fail_partial.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        try:
            setting = TestSetting(json_data)
            self.fail('Should throw KeyError!')
        except KeyError:
            pass

    @staticmethod
    def convert_request_to_dict(request):
        request_dict = {}
        if request.data:
            request_dict[request.KEY_DATA] = request.data
        if request.params:
            request_dict[request.KEY_PARAMS] = request.params
        if request.timeout:
            request_dict[request.KEY_TIMEOUT] = request.timeout
        if request.url:
            request_dict[request.KEY_URL] = request.url

        return request_dict

    @staticmethod
    def convert_response_to_dict(response):
        response_dict = {}
        if response.status_code:
            response_dict[response.KEY_STATUS_CODE] = response.status_code
        if response.json_schema:
            response_dict[response.KEY_JSON_SCHEMA] = response.json_schema

        return response_dict


if __name__ == '__main__':
    unittest.main()
