from . import TestFunction


class FailTestFunctionBuilder(object):
    """Build test function to let unittest know failure."""
    def __init__(self, msg, name):
        self._msg = msg
        self._name = name

    def build(self):
        def test_function(test_self):
            test_self.fail(self._msg)

        test_function_name = 'test_%s' % self._name
        return TestFunction(test_function_name, test_function)
