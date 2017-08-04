import unittest

from rest_tester.setting import TestMethod, SettingMethodError


class TestTestMethod(unittest.TestCase):
    def test_read_method(self):
        json_data = {
            "get": {}
        }

        test_method = TestMethod(json_data)
        self.assertEqual("get", test_method.read_method)

    def test_write_method(self):
        json_data = {
            "put": {}
        }

        test_method = TestMethod(json_data)
        self.assertEqual("put", test_method.write_method)

    def test_read_write_method(self):
        json_data = {
            "post": {},
            "get": {}
        }

        test_method = TestMethod(json_data)
        self.assertEqual("get", test_method.read_method)
        self.assertEqual("post", test_method.write_method)

    def test_invalid_two_methods(self):
        json_data = {
            "modify": {},
            "remove": {}
        }

        with self.assertRaises(SettingMethodError):
            TestMethod(json_data)

    def test_three_methods(self):
        json_data = {
            "post": {},
            "get": {},
            "put": {}
        }

        with self.assertRaises(SettingMethodError):
            TestMethod(json_data)

    def test_no_method(self):
        json_data = {
        }

        with self.assertRaises(SettingMethodError):
            TestMethod(json_data)

    def test_two_write_methods(self):
        json_data = {
            "post": {},
            "put": {}
        }

        with self.assertRaises(SettingMethodError):
            TestMethod(json_data)

if __name__ == '__main__':
    unittest.main()
