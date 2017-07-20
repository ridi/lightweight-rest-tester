from .method import TestMethod
from .request import Request
from .response import Response


class TestSetting(object):
    """Read test information from JSON data."""
    KEY_REQUEST = 'request'
    KEY_RESPONSE = 'response'

    def __init__(self, json_data):
        self._method = TestMethod(json_data)
        read_method = self._method.read_method
        write_method = self._method.write_method

        if read_method:
            try:
                self._read_request, self._read_response = self._read_setting(json_data[read_method])
            except KeyError:
                raise SettingIncompleteInformationError('%s has incomplete information.' % read_method)

        if write_method:
            try:
                self._write_request, self._write_response = self._read_setting(json_data[write_method])
            except KeyError:
                raise SettingIncompleteInformationError('%s has incomplete information.' % write_method)

    @classmethod
    def _read_setting(cls, json_data):
        request = Request(json_data[cls.KEY_REQUEST])
        response = Response(json_data[cls.KEY_RESPONSE])

        return request, response

    @property
    def method(self):
        return self._method

    @property
    def read_request(self):
        return self._read_request

    @property
    def read_response(self):
        return self._read_response

    @property
    def write_request(self):
        return self._write_request

    @property
    def write_response(self):
        return self._write_response


class SettingIncompleteInformationError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
