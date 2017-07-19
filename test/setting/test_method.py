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

        try:
            TestMethod(json_data)
            self.fail('Should throw KeyError!')
        except SettingMethodError:
            pass

    def test_three_methods(self):
        json_data = {
            "post": {},
            "get": {},
            "put": {}
        }

        try:
            TestMethod(json_data)
            self.fail('Should throw KeyError!')
        except SettingMethodError:
            pass

    def test_no_method(self):
        json_data = {
        }

        try:
            TestMethod(json_data)
            self.fail('Should throw KeyError!')
        except SettingMethodError:
            pass

    def test_two_write_methods(self):
        json_data = {
            "post": {},
            "put": {}
        }

        try:
            TestMethod(json_data)
            self.fail('Should throw KeyError!')
        except SettingMethodError:
            pass

if __name__ == '__main__':
    unittest.main()
