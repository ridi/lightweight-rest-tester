class Response(object):
    KEY_STATUS_CODE = 'statusCode'
    KEY_JSON_SCHEMA = 'jsonSchema'

    def __init__(self, response_data):
        self._status_code = response_data.get(self.KEY_STATUS_CODE)
        self._json_schema = response_data.get(self.KEY_JSON_SCHEMA)

        if (self._status_code or self._json_schema) is None:
            """One of them can be missing, but not all of them."""
            from rest_tester.setting import TestSetting
            raise KeyError(TestSetting.KEY_RESPONSE)

    @property
    def status_code(self):
        return self._status_code

    @property
    def json_schema(self):
        return self._json_schema
