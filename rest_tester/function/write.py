import json

from . import TestFunctionBuilder, TestFunction
from .read import ReadTestFunctionBuilder


class WriteTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from WRITE (e.g., PUT) method."""
    def build(self):
        if self._setting.method.read_method:
            return self._build_write_and_read()
        else:
            return self._build_write_only()

    def _build_write_and_read(self):
        write_request = self._setting.write_request
        write_response = self._setting.write_response

        def test_function(test_self):
            """Execute write-method functions first and then read-method functions"""
            write_function = self._build_test_function(write_request, write_response)
            write_function(test_self)

            read_builder = ReadTestFunctionBuilder(self._setting, self._name_prefix)
            read_function_list = read_builder.build()
            for read_function in read_function_list:
                read_function.test_function(test_self)

        test_function_name = self._generate_name(self._name_prefix, write_request)
        return [TestFunction(test_function_name, test_function)]

    def _build_write_only(self):
        write_request = self._setting.write_request
        write_response = self._setting.write_response

        return self._build_test_function_list(write_request, write_response)

    def _get_actual_response(self, request, params):
        data = json.dumps(request.data) if request.data else None
        write_method = self._setting.method.write_method

        response = self.send_request(method=write_method, url=request.url, params=params, timeout=request.timeout,
                                     data=data)
        return response
