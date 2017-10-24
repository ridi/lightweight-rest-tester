import copy

from rest_tester.setting import ParameterSet
from . import TestFunctionBuilder, TestFunction


class SingleTargetTestFunctionBuilder(TestFunctionBuilder):
    def __init__(self, setting):
        self._api = setting.targets[0].api
        self._tests = setting.targets[0].tests

    def build(self):
        test_function_list = []

        param_set_list = ParameterSet.generate(self._api.params)
        for param_set in param_set_list:
            curr_api = copy.deepcopy(self._api)
            curr_api.params = param_set

            test_function_name = self._generate_name(curr_api)
            test_function = self._build_test_function(test_function_name, curr_api, self._tests)
            test_function_list.append(TestFunction(test_function_name, test_function))

        return test_function_list
