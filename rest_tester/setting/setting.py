class TestSetting(object):
    """Read test information from JSON data."""
    KEY_METHOD = 'method'
    KEY_REQUEST = 'request'
    KEY_RESPONSE = 'response'

    METHOD_GET = 'get'
    METHOD_PUT = 'put'
    METHOD_POST = 'post'

    def __init__(self, json_data):
        self._method = json_data[self.KEY_METHOD]

        if self._method == self.METHOD_GET:
            self._read_request, self._read_response = self.read_setting(json_data, self.METHOD_GET)
            if self._read_request is None:
                raise KeyError(self.METHOD_GET)

        elif self._method == self.METHOD_PUT or self._method == self.METHOD_POST:
            """Read put- or post-method test case and get-method test case as well."""
            self._write_request, self._write_response = self.read_setting(json_data, self._method)
            if self._write_request is None:
                raise KeyError(self._method)

            """Get-method test case may by skipped."""
            self._read_request, self._read_response = self.read_setting(json_data, self.METHOD_GET)

        else:
            raise KeyError(self.KEY_METHOD)

    @classmethod
    def read_setting(cls, json_data, method_key):
        method_json_data = json_data.get(method_key)

        if method_json_data:
            """If method-related value exists, it should contain the keys of request and response."""
            from .request import Request
            from .response import Response

            request = Request(method_json_data[cls.KEY_REQUEST])
            response = Response(method_json_data[cls.KEY_RESPONSE])
        else:
            request = None
            response = None

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
