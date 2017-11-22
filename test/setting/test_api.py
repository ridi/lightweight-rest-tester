import unittest

from rest_tester.options import Options
from rest_tester.setting import API


class TestAPI(unittest.TestCase):
    def test_entire_information(self):
        api_data = {
            "url": "https://jsonplaceholder.typicode.com/comments",
            "method": "get",
            "params": {
                "postId": 1
            },
            "data": {
                "title": "foo",
                "body": "bar",
                "userId": 1
            }
        }

        api = API(api_data, Options())

        self.assertEqual(api_data['url'], api.url)
        self.assertEqual(api_data['method'], api.method)
        self.assertEqual(api_data['params'], api.params)
        self.assertEqual(api_data['data'], api.data)

    def test_essential_information(self):
        api_data = {
            "url": "https://jsonplaceholder.typicode.com/comments",
            "method": "get"
        }

        api = API(api_data, Options())

        self.assertEqual(api_data['url'], api.url)
        self.assertEqual(api_data['method'], api.method)

    def test_add_base_url(self):
        base_url = "https://jsonplaceholder.typicode.com"
        api_data = {
            "url": "/comments",
            "method": "get"
        }

        api = API(api_data, Options(base_url=base_url))

        self.assertEqual(base_url + api_data['url'], api.url)
        self.assertEqual(api_data['method'], api.method)

    def test_add_auth(self):
        user = 'user'
        password = 'pass'
        api_data = {
            "url": "/comments",
            "method": "get"
        }

        api = API(api_data, Options(auth=user + ':' + password))

        expected = (user, password)

        self.assertEqual(expected, api.auth)

    def test_add_insecure(self):
        insecure = True
        api_data = {
            "url": "/comments",
            "method": "get"
        }

        api = API(api_data, Options(insecure=insecure))

        self.assertTrue(api.insecure)

    def test_missing_information(self):
        api_data = {
            "params": {
                "postId": 1
            }
        }

        with self.assertRaises(KeyError):
            API(api_data, Options())

if __name__ == '__main__':
    unittest.main()
