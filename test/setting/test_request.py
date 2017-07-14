import unittest


from rest_tester.setting import Request


class TestRequest(unittest.TestCase):
    def test_success(self):
        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments",
            "params": {
                "postId": 1
            },
            "timeout": 10,
            "data": {
                "title": "foo",
                "body": "bar",
                "userId": 1
            }
        }

        request = Request(request_data)

        self.assertEqual(request_data['url'], request.url)
        self.assertEqual(request_data['params'], request.params)
        self.assertEqual(request_data['timeout'], request.timeout)
        self.assertEqual(request_data['data'], request.data)

    def test_success_partial(self):
        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments"
        }

        request = Request(request_data)

        self.assertEqual(request_data['url'], request.url)

    def test_fail(self):
        request_data = {
            "params": {
                "postId": 1
            },
            "timeout": 10
        }

        try:
            request = Request(request_data)
            self.fail('Should throw KeyError!')
        except KeyError:
            pass

if __name__ == '__main__':
    unittest.main()
