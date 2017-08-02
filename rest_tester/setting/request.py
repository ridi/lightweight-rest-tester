class Request(object):
    KEY_URL = 'url'
    KEY_PARAMS = 'params'
    KEY_DATA = 'data'

    def __init__(self, request_data):
        """Use get for only 'params' and 'timeout' to raise KeyError if keys do not exist."""
        self._url = request_data[self.KEY_URL]
        self._params = request_data.get(self.KEY_PARAMS, {})
        self._data = request_data.get(self.KEY_DATA)

        self._timeout = None

    @property
    def url(self):
        return self._url

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    @property
    def data(self):
        return self._data

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
