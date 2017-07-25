from rest_tester.setting.method import TestMethod, SettingMethodError, UnsupportedMethodError


class GenerationMethod(object):
    SUPPORT_TYPES = TestMethod.READ_TYPES | TestMethod.WRITE_TYPES

    def __init__(self, json_data):
        method_list = list(json_data)

        if len(method_list) != 1:
            raise SettingMethodError('Test case should have only one method for auto-generation!')

        self._method = method_list[0]
        if self._method not in self.SUPPORT_TYPES:
            raise UnsupportedMethodError('Unsupported read method: %s' % self._method)

    @property
    def method(self):
        return self._method
