import unittest


from rest_tester.setting import Request


class TestRequest(unittest.TestCase):
    def test_entire_information(self):
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

    def test_essential_information(self):
        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments"
        }

        request = Request(request_data)

        self.assertEqual(request_data['url'], request.url)

    def test_missing_information(self):
        request_data = {
            "params": {
                "postId": 1
            },
            "timeout": 10
        }

        try:
            Request(request_data)
        except KeyError:
            pass
        else:
            self.fail('Should throw KeyError!')

if __name__ == '__main__':
    unittest.main()
