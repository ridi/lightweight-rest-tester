import copy

import requests

from rest_tester.setting import ParameterSet, TestMethod
from . import TestFunctionBuilder, TestFunction


class ReadTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from READ (e.g., GET) method."""
    def __init__(self, setting, name_prefix):
        self._setting = setting
        self._name_prefix = name_prefix

    def build(self):
        request = self._setting.read_request
        response = self._setting.read_response

        test_function_list = []

        param_set_list = ParameterSet.generate(request.params)
        for param_set in param_set_list:
            curr_request = copy.deepcopy(request)
            curr_request.params = param_set

            test_function_name = self._generate_name(self._name_prefix, curr_request)
            test_function = self.build_test_function(curr_request, response)
            test_function_list.append(TestFunction(test_function_name, test_function))

        return test_function_list

    def _get_actual_response(self, request, params):
        read_method = self._setting.method.read_method
        if read_method == TestMethod.GET:
            return requests.get(url=request.url, params=params, timeout=request.timeout)
        else:
            raise ValueError
