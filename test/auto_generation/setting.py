from rest_tester.setting import Request, TestSetting, SettingIncompleteInformationError
from .method import GenerationMethod


class GenerationSetting(object):
    """Read test information from JSON data."""

    def __init__(self, json_data):
        self._method = GenerationMethod(json_data)
        method = self._method.method

        try:
            self._request = Request(json_data[method][TestSetting.KEY_REQUEST])
        except KeyError:
            raise SettingIncompleteInformationError('"%s" has incomplete information.' % method)

    @property
    def method(self):
        return self._method

    @property
    def request(self):
        return self._request
