import json

from rest_tester.test_info import TestInfo


def compare_two_lists(list1, list2):
    return len(list1) == len(list2) and \
           all(list1.count(i) == list2.count(i) for i in list1)


def load_test_info(json_file):
    with open(json_file, 'r') as json_file:
        json_data = json.load(json_file)
        return TestInfo.read(json_data)
