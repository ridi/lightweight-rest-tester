import unittest


from rest_tester.setting import Tests, SettingTestsError


class TestTests(unittest.TestCase):
    def test_entire_information(self):
        response_data = {
            "timeout": 10,
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

        response = Tests(response_data)

        self.assertEqual(response_data[Tests.KEY_TIMEOUT], response.timeout)
        self.assertEqual(response_data[Tests.KEY_STATUS_CODE], response.status_code)
        self.assertEqual(response_data[Tests.KEY_JSON_SCHEMA], response.json_schema)

    def test_essential_information(self):
        response_data = {
            "statusCode": 200
        }

        response = Tests(response_data)

        self.assertEqual(response_data[Tests.KEY_STATUS_CODE], response.status_code)

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
            Tests(response_data)
        except SettingTestsError:
            pass
        else:
            self.fail('Should throw KeyError!')

if __name__ == '__main__':
    unittest.main()
