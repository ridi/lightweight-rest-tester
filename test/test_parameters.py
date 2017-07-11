import unittest

from rest_tester.parameters import ParameterSet


class TestParameterSet(unittest.TestCase):
    def test_generate_no_list(self):
        params = {
            'param_1': 1,
            'param_2': 2,
            'param_3': 3
        }

        actual = ParameterSet.generate(params)
        expected = [params]

        self.assertTrue(self.compare_two_lists(actual, expected))

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

        self.assertTrue(self.compare_two_lists(actual, expected))

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

        self.assertTrue(self.compare_two_lists(actual, expected))

    @staticmethod
    def compare_two_lists(list1, list2):
        return len(list1) == len(list2) and \
               all(list1.count(i) == list2.count(i) for i in list1)

if __name__ == '__main__':
    unittest.main()
