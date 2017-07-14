import unittest


from rest_tester.setting import Response


class TestResponse(unittest.TestCase):
    def test_success(self):
        response_data = {
            "statusCode": 200,
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "postId": {
                        "type": "number"
                    }
                }
            }
        }

        response = Response(response_data)

        self.assertEqual(response_data['statusCode'], response.status_code)
        self.assertEqual(response_data['jsonSchema'], response.json_schema)

    def test_success_partial(self):
        response_data = {
            "statusCode": 200
        }

        response = Response(response_data)

        self.assertEqual(response_data['statusCode'], response.status_code)

    def test_fail(self):
        response_data = {
            "wrongStatusCode": 200,
            "wrongJsonSchema": {
                "type": "object",
                "properties": {
                    "postId": {
                        "type": "number"
                    }
                }
            }
        }

        try:
            request = Response(response_data)
            self.fail('Should throw KeyError!')
        except KeyError:
            pass

if __name__ == '__main__':
    unittest.main()
