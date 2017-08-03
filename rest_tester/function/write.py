import json

from rest_tester.setting import TestMethod, ParameterSet
from . import TestFunctionBuilder, TestFunction
from .read import ReadTestFunctionBuilder


class WriteTestFunctionBuilder(TestFunctionBuilder):
    """Build function that checks the response from WRITE (e.g., PUT) method."""
    def build(self):
        if self._setting.method.read_method:
            if self._setting.has_post_and_get_condition():
                return self._build_post_and_get()
            else:
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

    def _build_post_and_get(self):
        post_api = self._setting.write_api
        post_tests = self._setting.write_tests
        get_tests = self._setting.read_tests

        test_function_list = []

        param_set_list = ParameterSet.generate(post_api.params)
        for param_set in param_set_list:

            def test_function(test_self):
                post_timeout = post_tests.timeout
                post_response = self._get_response(post_api, param_set, post_timeout)

                self.run_test(test_self, post_tests, post_response)

                get_url = post_response.headers['Location']
                get_timeout = get_tests.timeout
                get_response = self._send_request(method=TestMethod.GET, url=get_url, params=None, timeout=get_timeout)

                self.run_test(test_self, get_tests, get_response)

            test_function_name = self._generate_name(self._name_prefix, post_api)
            test_function_list.append(TestFunction(test_function_name, test_function))

        return test_function_list

    def _build_write_only(self):
        write_api = self._setting.write_api
        write_tests = self._setting.write_tests

        return self._build_test_function_list(write_api, write_tests)

    def _get_response(self, api, params, timeout):
        data = json.dumps(api.data) if api.data else None
        write_method = self._setting.method.write_method

        return self._send_request(method=write_method, url=api.url, params=params, timeout=timeout, data=data)
