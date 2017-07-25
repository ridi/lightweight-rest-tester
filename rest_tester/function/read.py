from . import TestFunctionBuilder


class ReadTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from READ (e.g., GET) method."""
    def build(self):
        read_request = self._setting.read_request
        read_response = self._setting.read_response

        return self._build_test_function_list(read_request, read_response)

    def _get_actual_response(self, request, params):
        read_method = self._setting.method.read_method

        response = self.send_request(method=read_method, url=request.url, params=params, timeout=request.timeout)
        return response
