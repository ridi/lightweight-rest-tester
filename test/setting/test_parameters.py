import unittest

from rest_tester.setting import ParameterSet
from test import are_equal_lists


class TestParameterSet(unittest.TestCase):
    def test_generate_no_list(self):
        params = {
            'param_1': 1,
            'param_2': 2,
            'param_3': 3
        }

        actual = ParameterSet.generate(params)
        expected = [params]

        self.assertTrue(are_equal_lists(actual, expected))

    def test_generate_lists(self):
        params = {
            'param_1': [1, 2, 3],
            'param_2': ['a', 'b', 'c'],
            'param_3': ['def', 'efg', 'hij']
        }

        actual = ParameterSet.generate(params)
        expected = [
            {'param_1': 1, 'param_2': 'a', 'param_3': 'def'},
            {'param_1': 1, 'param_2': 'a', 'param_3': 'efg'},
            {'param_1': 1, 'param_2': 'a', 'param_3': 'hij'},

            {'param_1': 1, 'param_2': 'b', 'param_3': 'def'},
            {'param_1': 1, 'param_2': 'b', 'param_3': 'efg'},
            {'param_1': 1, 'param_2': 'b', 'param_3': 'hij'},

            {'param_1': 1, 'param_2': 'c', 'param_3': 'def'},
            {'param_1': 1, 'param_2': 'c', 'param_3': 'efg'},
            {'param_1': 1, 'param_2': 'c', 'param_3': 'hij'},


            {'param_1': 2, 'param_2': 'a', 'param_3': 'def'},
            {'param_1': 2, 'param_2': 'a', 'param_3': 'efg'},
            {'param_1': 2, 'param_2': 'a', 'param_3': 'hij'},

            {'param_1': 2, 'param_2': 'b', 'param_3': 'def'},
            {'param_1': 2, 'param_2': 'b', 'param_3': 'efg'},
            {'param_1': 2, 'param_2': 'b', 'param_3': 'hij'},

            {'param_1': 2, 'param_2': 'c', 'param_3': 'def'},
            {'param_1': 2, 'param_2': 'c', 'param_3': 'efg'},
            {'param_1': 2, 'param_2': 'c', 'param_3': 'hij'},


            {'param_1': 3, 'param_2': 'a', 'param_3': 'def'},
            {'param_1': 3, 'param_2': 'a', 'param_3': 'efg'},
            {'param_1': 3, 'param_2': 'a', 'param_3': 'hij'},

            {'param_1': 3, 'param_2': 'b', 'param_3': 'def'},
            {'param_1': 3, 'param_2': 'b', 'param_3': 'efg'},
            {'param_1': 3, 'param_2': 'b', 'param_3': 'hij'},

            {'param_1': 3, 'param_2': 'c', 'param_3': 'def'},
            {'param_1': 3, 'param_2': 'c', 'param_3': 'efg'},
            {'param_1': 3, 'param_2': 'c', 'param_3': 'hij'}
        ]

        self.assertTrue(are_equal_lists(actual, expected))

    def test_generate_lists_with_non_list(self):
        params = {
            'param_1': [1, 2, 3],
            'param_2': 'non_list_2',
            'param_3': ['a', 'b', 'c'],
            'param_4': 'non_list_4',
            'param_5': ['def', 'efg', 'hij']
        }

        actual = ParameterSet.generate(params)
        expected = [
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'def', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'def', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'def', 'param_3': 'c'},

            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'efg', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'efg', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'efg', 'param_3': 'c'},

            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'hij', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'hij', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 1, 'param_5': 'hij', 'param_3': 'c'},


            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'def', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'def', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'def', 'param_3': 'c'},

            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'efg', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'efg', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'efg', 'param_3': 'c'},

            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'hij', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'hij', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 2, 'param_5': 'hij', 'param_3': 'c'},


            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'def', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'def', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'def', 'param_3': 'c'},

            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'efg', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'efg', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'efg', 'param_3': 'c'},

            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'hij', 'param_3': 'a'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'hij', 'param_3': 'b'},
            {'param_4': 'non_list_4', 'param_2': 'non_list_2', 'param_1': 3, 'param_5': 'hij', 'param_3': 'c'}
        ]

        self.assertTrue(are_equal_lists(actual, expected))

if __name__ == '__main__':
    unittest.main()
