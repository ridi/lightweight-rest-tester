import requests
import json

from rest_tester.setting import TestMethod, UnsupportedMethodError
from . import TestFunctionBuilder, TestFunction
from .read import ReadTestFunctionBuilder


class WriteTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from WRITE (e.g., PUT) method."""
    def build(self):
        write_request = self._setting.write_request
        write_response = self._setting.write_response

        def test_function(test_self):
            write_function = self._build_test_function(write_request, write_response)
            write_function(test_self)

            if self._setting.method.read_method:
                """Some test cases may not call READ (e.g., GET) API."""
                read_builder = ReadTestFunctionBuilder(self._setting, self._name_prefix)
                read_function_list = read_builder.build()
                for read_function in read_function_list:
                    read_function.test_function(test_self)

        test_function_name = self._generate_name(self._name_prefix, write_request)
        return TestFunction(test_function_name, test_function)

    def _get_actual_response(self, request, params):
        url = request.url
        timeout = request.timeout
        data = json.dumps(request.data) if request.data else None
        headers = {'Content-Type': 'application/json'}

        write_method = self._setting.method.write_method
        if write_method == TestMethod.PUT:
            return requests.put(url=url, params=params, timeout=timeout, data=data, headers=headers)
        elif write_method == TestMethod.POST:
            return requests.post(url=url, params=params, timeout=timeout, data=data, headers=headers)
        elif write_method == TestMethod.PATCH:
            return requests.patch(url=url, params=params, timeout=timeout, data=data, headers=headers)
        elif write_method == TestMethod.DELETE:
            return requests.delete(url=url, params=params, timeout=timeout)
        else:
            raise UnsupportedMethodError('Unsupported read method: %s' % write_method)
