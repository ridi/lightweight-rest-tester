from abc import ABCMeta, abstractmethod
import jsonschema

from rest_tester.setting.parameters import ParameterSet
from rest_tester.utils import convert_to_list


class TestFunction(metaclass=ABCMeta):
    @staticmethod
    def test_status_code(self, expected_response, actual_response):
        """Check if the given status code is identical to the expected."""
        actual = actual_response.status_code
        expected = convert_to_list(expected_response.status_code)

        self.assertIn(actual, expected, 'Unexpected status code.')

    @staticmethod
    def test_json_schema(self, expected_response, actual_response):
        """Use jsonschema to validate the given JSON data is identical to the expected."""
        actual_json = actual_response.json()
        json_schema = expected_response.json_schema

        jsonschema.validate(actual_json, json_schema)

    @classmethod
    def make_test_function(cls, request, expected_response):
        """Make a test function"""
        def test_function(self):
            param_set_list = ParameterSet.generate(request.params)
            for param_set in param_set_list:
                """In some cases, the test case with all the combinations of parameters 
                    should be executed in one test case."""
                actual_response = cls.get_actual_response(request, param_set)

                if expected_response.status_code:
                    cls.test_status_code(self, expected_response, actual_response)

                if expected_response.json_schema:
                    cls.test_json_schema(self, expected_response, actual_response)

        return test_function

    @staticmethod
    def generate_name(base_name, request):
        """Test function name should start with 'test' since we use unit test."""
        param_str = '&'.join([key + "=" + str(value) for key, value in request.params.items()])
        if param_str != '':
            param_str = '?' + param_str

        return 'test_%s%s' % (base_name, param_str)

    @classmethod
    @abstractmethod
    def get_actual_response(cls, request, params):
        raise NotImplementedError
