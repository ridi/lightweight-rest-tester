from . import TestFunctionBuilder, TestFunction


class MultipleTargetsTestFunctionBuilder(TestFunctionBuilder):
    def __init__(self, setting):
        self._targets = setting.targets

    def build(self):
        test_function_name = self._generate_name(self._targets[0].api)

        def test_function_aggregated(test_self):
            for idx, target in enumerate(self._targets):
                curr_test_function_name = test_function_name + ' (%s)' % str(idx + 1)
                test_function = self._build_test_function(curr_test_function_name, target.api, target.tests)
                test_function(test_self)

        return [TestFunction(test_function_name, test_function_aggregated)]
