import unittest


from rest_tester.setting import API


class TestAPI(unittest.TestCase):
    def test_entire_information(self):
        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments",
            "params": {
                "postId": 1
            },
            "data": {
                "title": "foo",
                "body": "bar",
                "userId": 1
            }
        }

        request = API(request_data)

        self.assertEqual(request_data['url'], request.url)
        self.assertEqual(request_data['params'], request.params)
        self.assertEqual(request_data['data'], request.data)

    def test_essential_information(self):
        request_data = {
            "url": "https://jsonplaceholder.typicode.com/comments"
        }

        request = API(request_data)

        self.assertEqual(request_data['url'], request.url)

    def test_missing_information(self):
        request_data = {
            "params": {
                "postId": 1
            }
        }

        with self.assertRaises(KeyError):
            API(request_data)

if __name__ == '__main__':
    unittest.main()
