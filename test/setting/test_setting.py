import os
import unittest

from test.setting import convert_api_to_dict, convert_tests_to_dict
from rest_tester.setting import TestSetting, TestTarget
from test import load_json_data


class TestTestSetting(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_single(self):
        json_file = '%s/resources/test_setting_single.json' % self.current_dir_path
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertFalse(setting.has_multiple_targets())

        self.assertEqual(
                json_data[TestTarget.KEY_API],
                convert_api_to_dict(setting.targets[0].api)
        )
        self.assertEqual(
                json_data[TestTarget.KEY_TESTS],
                convert_tests_to_dict(setting.targets[0].tests)
        )

    def test_multiple(self):
        json_file = '%s/resources/test_setting_multiple.json' % self.current_dir_path
        json_data = load_json_data(json_file)

        setting = TestSetting(json_data)

        self.assertTrue(setting.has_multiple_targets())

        for idx, target in enumerate(setting.targets):
            self.assertEqual(
                    json_data[idx][TestTarget.KEY_API],
                    convert_api_to_dict(target.api)
            )
            self.assertEqual(
                    json_data[idx][TestTarget.KEY_TESTS],
                    convert_tests_to_dict(target.tests)
            )

if __name__ == '__main__':
    unittest.main()
