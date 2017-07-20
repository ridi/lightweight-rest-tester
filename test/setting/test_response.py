import unittest


from rest_tester.setting import Response, SettingResponseError


class TestResponse(unittest.TestCase):
    def test_entire_information(self):
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

    def test_essential_information(self):
        response_data = {
            "statusCode": 200
        }

        response = Response(response_data)

        self.assertEqual(response_data['statusCode'], response.status_code)

    def test_wrong_key(self):
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
            Response(response_data)
        except SettingResponseError:
            pass
        else:
            self.fail('Should throw KeyError!')

if __name__ == '__main__':
    unittest.main()
