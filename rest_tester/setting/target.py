from .api import API
from .tests import Tests


class TestTarget(object):
    KEY_API = 'api'
    KEY_TESTS = 'tests'

    def __init__(self, json_data):
        try:
            self._api = API(json_data[self.KEY_API])
            self._tests = Tests(json_data[self.KEY_TESTS])
        except KeyError:
            raise SettingIncompleteInformationError('Test case has incomplete information.')

    @property
    def api(self):
        return self._api

    @property
    def tests(self):
        return self._tests


class SettingIncompleteInformationError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
