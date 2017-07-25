import copy

import jsonschema
import requests

from rest_tester.setting import ParameterSet, UnsupportedMethodError, TestMethod
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
    def test_status_code(self, expected_response, actual_response):
        """Check if the given status code is identical to the expected."""
        actual = actual_response.status_code
        expected = convert_to_list(expected_response.status_code)

        self.assertIn(actual, expected, 'Unexpected status code.')

    @staticmethod
    def test_json_schema(self, expected_response, actual_response):
        """Use jsonschema to validate the given JSON data is identical to the expected."""
        actual_json = actual_response.json()
        json_schema = expected_response.json_schema

        jsonschema.validate(actual_json, json_schema)

    def _build_test_function(self, request, expected_response):
        def test_function(test_self):
            param_set_list = ParameterSet.generate(request.params)
            for param_set in param_set_list:
                """In some cases, the test case with all the combinations of parameters 
                    should be executed in one test case."""
                actual_response = self._get_actual_response(request, param_set)

                if expected_response.status_code:
                    self.test_status_code(test_self, expected_response, actual_response)

                if expected_response.json_schema:
                    self.test_json_schema(test_self, expected_response, actual_response)

        return test_function

    def _build_test_function_list(self, request, response):
        test_function_list = []

        param_set_list = ParameterSet.generate(request.params)
        for param_set in param_set_list:
            curr_request = copy.deepcopy(request)
            curr_request.params = param_set

            test_function_name = self._generate_name(self._name_prefix, curr_request)
            test_function = self._build_test_function(curr_request, response)
            test_function_list.append(TestFunction(test_function_name, test_function))

        return test_function_list

    @staticmethod
    def send_request(method, url, params, timeout, data=None):
        headers = {'Content-Type': 'application/json'}

        if method == TestMethod.GET:
            return requests.get(url=url, params=params, timeout=timeout)
        elif method == TestMethod.PUT:
            return requests.put(url=url, params=params, timeout=timeout, data=data, headers=headers)
        elif method == TestMethod.POST:
            return requests.post(url=url, params=params, timeout=timeout, data=data, headers=headers)
        elif method == TestMethod.PATCH:
            return requests.patch(url=url, params=params, timeout=timeout, data=data, headers=headers)
        elif method == TestMethod.DELETE:
            return requests.delete(url=url, params=params, timeout=timeout)
        else:
            raise UnsupportedMethodError('Unsupported read method: %s' % method)

    @staticmethod
    def _generate_name(name_prefix, request):
        """Test function name should start with 'test' since we use unit test."""
        param_str = '&'.join([key + "=" + str(value) for key, value in request.params.items()])
        if param_str != '':
            param_str = '?' + param_str

        return 'test_%s%s' % (name_prefix, param_str)

    def build(self):
        raise NotImplementedError

    def _get_actual_response(self, request, params):
        raise NotImplementedError
