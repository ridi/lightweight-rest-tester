class API(object):
    KEY_URL = 'url'
    KEY_PARAMS = 'params'
    KEY_DATA = 'data'

    def __init__(self, api_data):
        """Use get for only 'params' and 'timeout' to raise KeyError if keys do not exist."""
        self._url = api_data[self.KEY_URL]
        self._params = api_data.get(self.KEY_PARAMS, {})
        self._data = api_data.get(self.KEY_DATA)

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
