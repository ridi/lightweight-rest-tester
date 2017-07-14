import requests

from . import TestFunction
from .get import GetTestFunction


class PutTestFunction(TestFunction):
    @classmethod
    def make(cls, put_request, put_response, get_request, get_response):
        def test_function(self):
            post_function = cls.make_test_function(put_request, put_response)
            post_function(self)

            if get_request and get_response:
                """Some test cases may not call get API."""
                get_function = GetTestFunction.make(get_request, get_response)
                get_function(self)

        return test_function

    @classmethod
    def get_actual_response(cls, request, params):
        return requests.put(url=request.url, params=params, timeout=request.timeout, data=request.data)
