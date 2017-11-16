import json
import abc

import jsonschema
import requests

from rest_tester.setting import ParameterSet, TestMethod, UnsupportedMethodError
from rest_tester.utils import convert_to_list


class TestFunction(object):
    """Contains test function and its name"""
    def __init__(self, name, test_function):
        self._name = name
        self._test_function = test_function

    @property
    def name(self):
        return self._name

    @property
    def test_function(self):
        return self._test_function


class TestFunctionBuilderFactory(object):
    @staticmethod
    def get_builder(setting):
        if setting.has_multiple_targets():
            from .multiple import MultipleTargetsTestFunctionBuilder
            return MultipleTargetsTestFunctionBuilder(setting)

        else:
            from .single import SingleTargetTestFunctionBuilder
            return SingleTargetTestFunctionBuilder(setting)


class TestFunctionBuilder(object):
    """Build test functions"""
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def _run_tests(self, tests, response):
        if tests.status_code:
            self.assertIn(
                    response.status_code,
                    convert_to_list(tests.status_code),
                    'Unexpected status code.'
            )

        if tests.json_schema:
            jsonschema.validate(
                    response.json(),
                    tests.json_schema
            )

    def _build_test_function(self, name, api, tests):
        def test_function(test_self):
            param_set_list = ParameterSet.generate(api.params)
            for param_set in param_set_list:
                timeout = tests.timeout
                response = self._get_response(api, param_set, timeout)

                response_time = response.elapsed.total_seconds()
                print(name + ' takes ' + str(round(response_time, 4)) + ' seconds.')

                self._run_tests(test_self, tests, response)

        return test_function

    def _get_response(self, api, params, timeout):
        data = json.dumps(api.data) if api.data else None

        return self._send_request(method=api.method, url=api.url, params=params, timeout=timeout, data=data,
                                  auth=api.auth)

    @staticmethod
    def _send_request(method, url, params, timeout, data, auth):
        headers = {'Content-Type': 'application/json'}

        print(str(auth))

        if method == TestMethod.GET:
            return requests.get(url=url, params=params, timeout=timeout, auth=auth)
        elif method == TestMethod.PUT:
            return requests.put(url=url, params=params, timeout=timeout, data=data, headers=headers, auth=auth)
        elif method == TestMethod.POST:
            return requests.post(url=url, params=params, timeout=timeout, data=data, headers=headers, auth=auth)
        elif method == TestMethod.PATCH:
            return requests.patch(url=url, params=params, timeout=timeout, data=data, headers=headers, auth=auth)
        elif method == TestMethod.DELETE:
            return requests.delete(url=url, params=params, timeout=timeout, auth=auth)
        else:
            raise UnsupportedMethodError('Unsupported method: %s' % method)

    @staticmethod
    def _generate_name(api):
        """Test function name should start with 'test' since we use unit test."""
        param_str = '&'.join([key + "=" + str(value) for key, value in api.params.items()])
        if param_str != '':
            param_str = '?' + param_str

        return 'test_%s%s' % (api.url, param_str)

    @abc.abstractmethod
    def build(self):
        raise NotImplementedError
