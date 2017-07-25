import requests

from rest_tester.setting import TestMethod, UnsupportedMethodError
from . import TestFunctionBuilder


class ReadTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from READ (e.g., GET) method."""
    def build(self):
        read_request = self._setting.read_request
        read_response = self._setting.read_response

        return self._build_test_function_list(read_request, read_response)

    def _get_actual_response(self, request, params):
        read_method = self._setting.method.read_method
        if read_method == TestMethod.GET:
            return requests.get(url=request.url, params=params, timeout=request.timeout)
        else:
            raise UnsupportedMethodError('Unsupported read method: %s' % read_method)
