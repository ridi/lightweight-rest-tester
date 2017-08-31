import os
import unittest

from rest_tester.options import Options
from test.setting import convert_api_to_dict, convert_tests_to_dict
from rest_tester.setting import TestTarget, IncompleteTargetInformationError
from test import load_json_data


class TestTestTarget(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_target(self):
        json_file = '%s/resources/test_target.json' % self.current_dir_path
        json_data = load_json_data(json_file)

        test_target = TestTarget(json_data, Options())

        self.assertEqual(
                json_data[TestTarget.KEY_API],
                convert_api_to_dict(test_target.api)
        )
        self.assertEqual(
                json_data[TestTarget.KEY_TESTS],
                convert_tests_to_dict(test_target.tests)
        )

    def test_target_missing_response(self):
        json_file = '%s/resources/test_target_missing_response.json' % self.current_dir_path
        json_data = load_json_data(json_file)

        with self.assertRaises(IncompleteTargetInformationError):
            TestTarget(json_data, Options())


if __name__ == '__main__':
    unittest.main()
