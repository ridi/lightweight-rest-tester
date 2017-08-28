from . import TestFunction, TestFunctionBuilder


class FailTestFunctionBuilder(TestFunctionBuilder):
    """Build test function to let unittest know failure."""
    def __init__(self, msg, name_prefix):
        super(FailTestFunctionBuilder, self).__init__(name_prefix)

        self._msg = msg

    def build(self):
        def test_function(test_self):
            test_self.fail(self._msg)

        test_function_name = 'test_%s' % self._name_prefix
        return TestFunction(test_function_name, test_function)
