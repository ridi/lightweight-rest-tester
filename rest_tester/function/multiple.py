from . import TestFunctionBuilder, TestFunction


class MultipleTargetsTestFunctionBuilder(TestFunctionBuilder):
    def __init__(self, setting, name_prefix):
        TestFunctionBuilder.__init__(self, name_prefix)

        self.targets = setting.targets

    def build(self):
        def test_function_aggregated(test_self):
            for target in self.targets:
                test_function = self._build_test_function(target.api, target.tests)
                test_function(test_self)

        test_function_name = self._generate_name(self._name_prefix, self.targets[0].api)
        return [TestFunction(test_function_name, test_function_aggregated)]
