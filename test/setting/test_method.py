import unittest

from rest_tester.setting import TestMethod, UnsupportedMethodError


class TestTestMethod(unittest.TestCase):
    def test_get_method(self):
        method_get = 'get'

        test_method = TestMethod(method_get)
        self.assertEqual(method_get, test_method.method)

    def test_post_method(self):
        method_post = 'post'

        test_method = TestMethod(method_post)
        self.assertEqual(method_post, test_method.method)

    def test_put_method(self):
        method_put = 'put'

        test_method = TestMethod(method_put)
        self.assertEqual(method_put, test_method.method)

    def test_patch_method(self):
        method_patch = 'patch'

        test_method = TestMethod(method_patch)
        self.assertEqual(method_patch, test_method.method)

    def test_delete_method(self):
        method_delete = 'delete'

        test_method = TestMethod(method_delete)
        self.assertEqual(method_delete, test_method.method)

    def test_no_method(self):
        with self.assertRaises(UnsupportedMethodError):
            TestMethod('')

    def test_invalid_method(self):
        with self.assertRaises(UnsupportedMethodError):
            TestMethod('modify')

if __name__ == '__main__':
    unittest.main()
