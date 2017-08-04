import unittest


from rest_tester.setting import Tests, SettingTestsError


class TestTests(unittest.TestCase):
    def test_entire_information(self):
        tests_data = {
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

        response = Tests(tests_data)

        self.assertEqual(tests_data[Tests.KEY_TIMEOUT], response.timeout)
        self.assertEqual(tests_data[Tests.KEY_STATUS_CODE], response.status_code)
        self.assertEqual(tests_data[Tests.KEY_JSON_SCHEMA], response.json_schema)

    def test_essential_information(self):
        tests_data = {
            "statusCode": 200
        }

        response = Tests(tests_data)

        self.assertEqual(tests_data[Tests.KEY_STATUS_CODE], response.status_code)

    def test_wrong_key(self):
        tests_data = {
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

        with self.assertRaises(SettingTestsError):
            Tests(tests_data)

if __name__ == '__main__':
    unittest.main()
