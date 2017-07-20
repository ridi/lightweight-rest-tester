import unittest


from rest_tester.utils import convert_to_list
from test.helper import are_equal_lists


class TestUtils(unittest.TestCase):
    def test_convert_to_list(self):
        actual = convert_to_list('item')
        expected = ['item']

        self.assertTrue(are_equal_lists(actual, expected))

    def test_convert_to_list_by_list(self):
        actual = convert_to_list(['item'])
        expected = ['item']

        self.assertTrue(are_equal_lists(actual, expected))

if __name__ == '__main__':
    unittest.main()
