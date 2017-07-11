import requests
import jsonschema


class Response(object):
    """Get content and status code of responses."""
    @staticmethod
    def get_response_status_code(url, params, timeout):
        """Get the HTTP status code from the request"""
        return requests.get(url=url, params=params, timeout=timeout).status_code if url else None

    @staticmethod
    def get_response_content(url, params, timeout):
        """Get the content from the request"""
        response = requests.get(url=url, params=params, timeout=timeout) if url else None
        return response.json() if response else {}


class TestFunction(object):
    """Make test functions and generate their names."""
    @staticmethod
    def generate_name(file_name, test_key, params):
        """Test function name should start with 'test' since we use unit test."""
        param_str = None
        for key in params.keys():
            curr_str = key + "=" + str(params[key])
            if param_str is None:
                param_str = '?' + curr_str
            else:
                param_str += "&" + curr_str

        if param_str is None:
            param_str = ''

        return 'test_%s_%s%s' % (file_name, test_key, param_str)

    @staticmethod
    def make(url, params, timeout, test_key, test_case):
        """Make a test function"""
        def test_status_code(self):
            actual = Response.get_response_status_code(url, params, timeout)
            expected = test_case if type(test_case) is list else [test_case]

            self.assertIn(actual, expected, 'Unexpected status code.')

        def test_json_schema(self):
            actual = Response.get_response_content(url, params, timeout)
            expected = test_case

            jsonschema.validate(actual, expected)

        test_functions = {
            'statusCode': test_status_code,
            'jsonSchema': test_json_schema
        }

        """If test cases are not supported, let them cause assert error."""
        def test_unsupported_case(self):
            self.assertIn(test_key, test_functions.keys(), 'Unsupported test case.')

        if test_key not in test_functions.keys():
            return test_unsupported_case

        return test_functions[test_key]


class TestFailFunction(object):
    @staticmethod
    def generate_name(file_name):
        """Test function name should start with 'test' since we use unit test."""
        return 'test_%s' % file_name

    @staticmethod
    def make(msg):
        """Make a test function"""

        def test_fail(self):
            self.fail(msg)

        return test_fail
