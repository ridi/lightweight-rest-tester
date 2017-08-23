from . import TestFunctionBuilder


class SingleTargetTestFunctionBuilder(TestFunctionBuilder):
    def __init__(self, setting, name_prefix):
        TestFunctionBuilder.__init__(self, name_prefix)

        self.api = setting.targets[0].api
        self.tests = setting.targets[0].tests

    def build(self):
        return self._build_test_function_list(self.api, self.tests)
