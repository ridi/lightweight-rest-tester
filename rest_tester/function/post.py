import requests
import json

from . import TestFunction
from .get import GetTestFunction


class PostTestFunction(TestFunction):
    headers = {'Content-Type': 'application/json'}

    @classmethod
    def make(cls, post_request, post_response, get_request, get_response):
        def test_function(self):
            post_function = cls.make_test_function(post_request, post_response)
            post_function(self)

            if get_request and get_response:
                """Some test cases may not call get API."""
                get_function = GetTestFunction.make(get_request, get_response)
                get_function(self)

        return test_function

    @classmethod
    def get_actual_response(cls, request, params):
        return requests.post(url=request.url, params=params, timeout=request.timeout, data=json.dumps(request.data),
                             headers=cls.headers)
