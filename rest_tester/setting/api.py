from .method import TestMethod


class API(object):
    KEY_URL = 'url'
    KEY_METHOD = 'method'
    KEY_PARAMS = 'params'
    KEY_DATA = 'data'

    def __init__(self, api_data, options):
        self._url = api_data[self.KEY_URL]
        self._method = TestMethod(api_data[self.KEY_METHOD])
        self._params = api_data.get(self.KEY_PARAMS, {})
        self._data = api_data.get(self.KEY_DATA)

        self._options = options

    @property
    def url(self):
        if self._options.base_url is not None:
            return self._options.base_url + self._url

        return self._url

    @property
    def method(self):
        return self._method.method

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
    def auth(self):
        return self._options.auth

    @property
    def insecure(self):
        return self._options.insecure
