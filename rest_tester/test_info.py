class TestInfo(object):
    """Read test information from JSON data."""
    PATH_API = 'api'

    PATH_API_URL = 'url'
    PATH_API_PARAMS = 'params'
    PATH_API_TIMEOUT = 'timeout'

    PATH_TESTS = 'tests'

    DEFAULT_TIME_OUT = 10

    @classmethod
    def read(cls, json_data):
        """Read test information from JSON data."""
        api_data = json_data[cls.PATH_API]

        url = api_data[cls.PATH_API_URL]
        params = api_data[cls.PATH_API_PARAMS] if cls.PATH_API_PARAMS in api_data.keys() else {}
        timeout = api_data[cls.PATH_API_TIMEOUT] if cls.PATH_API_TIMEOUT in api_data.keys() else cls.DEFAULT_TIME_OUT

        test_cases = json_data[cls.PATH_TESTS]

        return url, params, timeout, test_cases
