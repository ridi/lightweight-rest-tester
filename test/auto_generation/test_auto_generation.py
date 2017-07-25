import os
import unittest

from test import helper
from test.auto_generation.setting import GenerationSetting


class TestTestSetting(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_generate(self):
        json_file = '%s/resources/test_auto_generation_get_simple.json' % self.current_dir_path
        json_data = helper.load_json_data(json_file)

        setting = GenerationSetting(json_data)

if __name__ == '__main__':
    unittest.main()
