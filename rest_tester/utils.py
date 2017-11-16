import json


def convert_to_list(value):
    """Convert value to list if not"""
    if isinstance(value, list):
        return value
    else:
        return [value]


def read_json_file(file):
    with open(file=file) as json_file:
        return json.load(json_file)
