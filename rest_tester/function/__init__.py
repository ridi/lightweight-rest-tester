import copy

import jsonschema

from rest_tester.setting import ParameterSet, UnsupportedMethodError
from rest_tester.utils import convert_to_list


class TestFunction(object):
    """Contains test function and its name"""
    def __init__(self, name, test_function):
        self._name = name
        self._test_function = test_function

    @property
    def name(self):
        return self._name

    @property
    def test_function(self):
        return self._test_function


class TestFunctionBuilderFactory(object):
    @staticmethod
    def get_builder(setting, name_prefix):
        if setting.method.write_method:
            from .write import WriteTestFunctionBuilder
            return WriteTestFunctionBuilder(setting, name_prefix)

        elif setting.method.read_method:
            from .read import ReadTestFunctionBuilder
            return ReadTestFunctionBuilder(setting, name_prefix)

        else:
            raise UnsupportedMethodError


class TestFunctionBuilder(object):
    """Build test functions"""
    def __init__(self, setting, name_prefix):
        self._setting = setting
        self._name_prefix = name_prefix

    @staticmethod
    def validate_status_code(self, expected, response):
        """Check if the given status code is identical to the expected."""
        actual = response.status_code

        self.assertIn(actual, convert_to_list(expected), 'Unexpected status code.')

    @staticmethod
    def validate_json(self, json_schema, response):
        """Use jsonschema to validate the given JSON data is identical to the expected."""
        actual_json = response.json()

        jsonschema.validate(actual_json, json_schema)

    def _build_test_function(self, api, tests):
        def test_function(test_self):
            param_set_list = ParameterSet.generate(api.params)
            for param_set in param_set_list:
                """In some cases, the test case with all the combinations of parameters 
                    should be executed in one test case."""
                timeout = tests.timeout
                response = self._get_response(api, param_set, timeout)

                if tests.status_code:
                    self.validate_status_code(test_self, tests.status_code, response)

                if tests.json_schema:
                    self.validate_json(test_self, tests.json_schema, response)

        return test_function

    def _build_test_function_list(self, api, tests):
        test_function_list = []

        param_set_list = ParameterSet.generate(api.params)
        for param_set in param_set_list:
            curr_api = copy.deepcopy(api)
            curr_api.params = param_set

            test_function_name = self._generate_name(self._name_prefix, curr_api)
            test_function = self._build_test_function(curr_api, tests)
            test_function_list.append(TestFunction(test_function_name, test_function))

        return test_function_list

    @staticmethod
    def _generate_name(name_prefix, request):
        """Test function name should start with 'test' since we use unit test."""
        param_str = '&'.join([key + "=" + str(value) for key, value in request.params.items()])
        if param_str != '':
            param_str = '?' + param_str

        return 'test_%s%s' % (name_prefix, param_str)

    def build(self):
        raise NotImplementedError

    def _get_response(self, request, params, timeout):
        raise NotImplementedError
