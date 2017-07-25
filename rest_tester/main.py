import glob
import json
import os
import sys
import unittest

from rest_tester.function import TestFunctionBuilderFactory
from rest_tester.function.fail import FailTestFunctionBuilder
from rest_tester.setting import TestSetting


class TestsContainer(unittest.TestCase):
    """The test container for dynamically generated test cases."""
    longMessage = True


def identify_files_in_dir(path):
    """Identify the json files in the given directory recursively."""
    return [target for file_path in os.walk(path) for target in glob.glob(os.path.join(file_path[0], '*.json'))]


def add_function_to_container(test_function):
    """Add test functions with their name to container"""
    setattr(TestsContainer, test_function.name, test_function.test_function)
    print('%s is added to the test container.' % test_function.name)


def main(argv):
    """Read test_suites_dir from the arguments."""
    try:
        script, test_suites_dir = argv
    except ValueError:
        print('Please specify the test suite directory for testing.')
        raise

    for test_case_file in identify_files_in_dir(test_suites_dir):
        print('Working on %s ...' % test_case_file)
        file_name = os.path.basename(test_case_file)

        def add_fail_function(msg):
            fail_function_builder = FailTestFunctionBuilder(msg, file_name)
            fail_function = fail_function_builder.build()
            add_function_to_container(fail_function)

        try:
            json_file = open(test_case_file)
            json_data = json.load(json_file)
        except Exception as file_error:
            add_fail_function('Cannot parse the json file: %s' % str(file_error))
            continue

        try:
            setting = TestSetting(json_data)
        except Exception as setting_error:
            add_fail_function(str(setting_error))
            continue

        test_function_builder = TestFunctionBuilderFactory.get_builder(setting, file_name)
        test_function_list = test_function_builder.build()
        for test_function in test_function_list:
            add_function_to_container(test_function)

    suite = unittest.makeSuite(TestsContainer)
    unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ == '__main__':
    main(sys.argv)
