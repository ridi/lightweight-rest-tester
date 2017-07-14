import copy
import glob
import json
import os
import sys
import unittest

from rest_tester.function.fail import FailTestFunction
from rest_tester.function.get import GetTestFunction
from rest_tester.function.post import PostTestFunction
from rest_tester.function.put import PutTestFunction
from rest_tester.setting import TestSetting, ParameterSet


class TestsContainer(unittest.TestCase):
    """The test container for dynamically generated test cases."""
    longMessage = True


def identify_files_in_dir(path):
    """Identify the json files in the given directory recursively."""
    return [target for file_path in os.walk(path) for target in glob.glob(os.path.join(file_path[0], '*.json'))]


def add_function_to_container(name, test_function):
    """Add test functions with their name to container"""
    setattr(TestsContainer, name, test_function)
    print('%s is added to the test container.' % name)


if __name__ == '__main__':
    """Read test_suites_dir from the arguments."""
    try:
        script, test_suites_dir = sys.argv
    except ValueError:
        print('Please specify the test suite directory for testing.')
        raise

    for test_case_file in identify_files_in_dir(test_suites_dir):
        print('Working on %s ...' % test_case_file)
        file_name = os.path.basename(test_case_file)

        def add_fail_function(msg):
            """Add fail function when cannot read test setting."""
            fail_function_name = FailTestFunction.generate_name(file_name)
            fail_function = FailTestFunction.make(msg)
            add_function_to_container(fail_function_name, fail_function)

        try:
            json_file = open(test_case_file)
            json_data = json.load(json_file)
        except Exception:
            add_fail_function('Cannot parse the json file.')
            continue

        try:
            setting = TestSetting(json_data)
        except KeyError as key_error:
            add_fail_function('Essential test setting is missing: %s' % str(key_error))
            continue

        def add_get_method():
            """Generate test functions of get-method."""
            request = setting.read_request

            """We want to make a test case for each parameter set if possible."""
            param_set_list = ParameterSet.generate(request.params)
            for param_set in param_set_list:
                curr_request = copy.deepcopy(request)
                curr_request.params = param_set

                test_function_name = GetTestFunction.generate_name(file_name, curr_request)
                test_function = GetTestFunction.make(curr_request, setting.read_response)
                add_function_to_container(test_function_name, test_function)

        def add_put_method():
            """Generate test functions of put-method."""
            test_function_name = PutTestFunction.generate_name(file_name, setting.write_request)
            test_function = PutTestFunction.make(setting.write_request, setting.write_response,
                                                 setting.read_request, setting.read_response)
            add_function_to_container(test_function_name, test_function)

        def add_post_method():
            """Generate test functions of post-method."""
            test_function_name = PostTestFunction.generate_name(file_name, setting.write_request)
            test_function = PostTestFunction.make(setting.write_request, setting.write_response,
                                                  setting.read_request, setting.read_response)
            add_function_to_container(test_function_name, test_function)

        add_test_functions = {
            TestSetting.METHOD_GET: add_get_method,
            TestSetting.METHOD_PUT: add_put_method,
            TestSetting.METHOD_POST: add_post_method
        }

        add_test_functions[setting.method]()

    suite = unittest.makeSuite(TestsContainer)
    unittest.TextTestRunner(verbosity=1).run(suite)
