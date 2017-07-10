class TestInfo(object):
    """Read test information from JSON data."""
    PATH_API = 'api'

    PATH_API_URL = 'url'
    PATH_API_PARAMS = 'params'
    PATH_API_TIMEOUT = 'timeout'

    PATH_TESTS = 'tests'

    @classmethod
    def read(cls, json_data):
        """Read test information from JSON data."""
        api_data = json_data[cls.PATH_API]

        url = api_data[cls.PATH_API_URL]
        params = api_data[cls.PATH_API_PARAMS]
        timeout = api_data[cls.PATH_API_TIMEOUT]

        test_cases = json_data[cls.PATH_TESTS]

        return url, params, timeout, test_cases
