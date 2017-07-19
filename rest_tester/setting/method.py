class TestMethod(object):
    GET = 'get'

    PUT = 'put'
    POST = 'post'
    PATCH = 'patch'
    DELETE = 'delete'

    READ_TYPES = {GET}
    WRITE_TYPES = {PUT, POST, PATCH, DELETE}

    def __init__(self, json_data):
        method_list = list(json_data)

        method_num = len(method_list)
        if method_num <= 0:
            raise SettingMethodError('Test case should have at least one method!')

        if method_num > 2:
            raise SettingMethodError('Test case cannot have more than two methods!')

        self._read_method = self._identify_method(method_list, self.READ_TYPES)
        self._write_method = self._identify_method(method_list, self.WRITE_TYPES)

        if self._read_method is None and self._write_method is None:
            raise SettingMethodError('Test case should have at least one READ (e.g., GET) or WRITE (e.g., PUT) method!')

        if method_num == 2:
            if self._read_method is None:
                raise SettingMethodError('READ (e.g., GET) method is expected, but missing')
            if self._write_method is None:
                raise SettingMethodError('WRITE (e.g., PUT) method is expected, but missing')

    @property
    def read_method(self):
        return self._read_method

    @property
    def write_method(self):
        return self._write_method

    @classmethod
    def _identify_method(cls, method_list, method_types):
        for method in method_list:
            if method in method_types:
                return method

        return None


class SettingMethodError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class UnsupportedMethodError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
