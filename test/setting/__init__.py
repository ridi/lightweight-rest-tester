def convert_api_to_dict(api):
    api_dict = {}
    if api.data:
        api_dict[api.KEY_DATA] = api.data
    if api.params:
        api_dict[api.KEY_PARAMS] = api.params
    if api.method:
        api_dict[api.KEY_METHOD] = api.method
    if api.url:
        api_dict[api.KEY_URL] = api.url

    return api_dict


def convert_tests_to_dict(tests):
    tests_dict = {}
    if tests.timeout:
        tests_dict[tests.KEY_TIMEOUT] = tests.timeout
    if tests.status_code:
        tests_dict[tests.KEY_STATUS_CODE] = tests.status_code
    if tests.json_schema:
        tests_dict[tests.KEY_JSON_SCHEMA] = tests.json_schema

    return tests_dict
