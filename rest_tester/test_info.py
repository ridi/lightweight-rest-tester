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
        """Use get for only 'params' and 'timeout' to raise KeyError if keys do not exist."""
        api_data = json_data[cls.PATH_API]

        url = api_data[cls.PATH_API_URL]
        params = api_data.get(cls.PATH_API_PARAMS, {})
        timeout = api_data.get(cls.PATH_API_TIMEOUT, cls.DEFAULT_TIME_OUT)

        test_cases = json_data[cls.PATH_TESTS]

        return url, params, timeout, test_cases
