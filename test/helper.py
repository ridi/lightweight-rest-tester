import json


def are_equal_lists(list1, list2):
    """Check if two lists contain same items regardless of their orders."""
    return len(list1) == len(list2) and all(list1.count(i) == list2.count(i) for i in list1)


def load_json_data(json_file):
    with open(json_file, 'r') as json_file:
        return json.load(json_file)
