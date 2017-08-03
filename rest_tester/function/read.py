from . import TestFunctionBuilder


class ReadTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from READ (e.g., GET) method."""
    def build(self):
        read_api = self._setting.read_api
        read_tests = self._setting.read_tests

        return self._build_test_function_list(read_api, read_tests)

    def _get_response(self, api, params, timeout):
        read_method = self._setting.method.read_method

        return self._send_request(method=read_method, url=api.url, params=params, timeout=timeout)
