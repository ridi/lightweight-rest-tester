import requests
import json

from rest_tester.setting import TestMethod, UnsupportedMethodError
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
        write_api = self._setting.write_api
        write_tests = self._setting.write_tests

        def test_function(test_self):
            """Execute write-method functions first and then read-method functions"""
            write_function = self._build_test_function(write_api, write_tests)
            write_function(test_self)

            read_builder = ReadTestFunctionBuilder(self._setting, self._name_prefix)
            read_function_list = read_builder.build()
            for read_function in read_function_list:
                read_function.test_function(test_self)

        test_function_name = self._generate_name(self._name_prefix, write_api)
        return [TestFunction(test_function_name, test_function)]

    def _build_write_only(self):
        write_api = self._setting.write_api
        write_tests = self._setting.write_tests

        return self._build_test_function_list(write_api, write_tests)

    def _get_response(self, api, params, timeout):
        url = api.url
        data = json.dumps(api.data) if api.data else None
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
