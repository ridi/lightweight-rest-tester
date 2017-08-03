from .method import TestMethod
from .api import API
from .tests import Tests


class TestSetting(object):
    """Read test information from JSON data."""
    KEY_API = 'api'
    KEY_TESTS = 'tests'

    def __init__(self, json_data):
        self._method = TestMethod(json_data)
        write_method = self._method.write_method
        read_method = self._method.read_method

        if write_method:
            try:
                self._write_api, self._write_tests = self._read_setting(json_data[write_method])
            except KeyError:
                raise SettingIncompleteInformationError('"%s" has incomplete information.' % write_method)

        if read_method:
            try:
                self._read_api, self._read_tests = self._read_setting(json_data[read_method])
            except KeyError:
                raise SettingIncompleteInformationError('"%s" has incomplete information.' % read_method)

            if self._read_api is None and not self.has_post_and_get_condition():
                raise SettingIncompleteInformationError('"%s.%s" can be omitted only for POST-and-GET.' %
                                                        (read_method, self.KEY_API))

    @classmethod
    def _read_setting(cls, json_data):
        """API can be missing for POST-and-GET, but Tests should not be missing."""
        api_data = json_data.get(cls.KEY_API)
        api = API(api_data) if api_data else None

        tests = Tests(json_data[cls.KEY_TESTS])

        return api, tests

    @property
    def method(self):
        return self._method

    @property
    def read_api(self):
        return self._read_api

    @property
    def read_tests(self):
        return self._read_tests

    @property
    def write_api(self):
        return self._write_api

    @property
    def write_tests(self):
        return self._write_tests

    def has_post_and_get_condition(self):
        if self._read_api is None and self._method.write_method == TestMethod.POST:
            return True
        else:
            return False


class SettingIncompleteInformationError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
