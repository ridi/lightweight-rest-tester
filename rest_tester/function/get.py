import requests

from . import TestFunction


class GetTestFunction(TestFunction):
    @classmethod
    def make(cls, request, response):
        """Make a test function"""
        return cls.make_test_function(request, response)

    @classmethod
    def get_actual_response(cls, request, params):
        return requests.get(url=request.url, params=params, timeout=request.timeout)
