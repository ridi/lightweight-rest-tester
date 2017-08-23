class TestMethod(object):
    GET = 'get'
    PUT = 'put'
    POST = 'post'
    PATCH = 'patch'
    DELETE = 'delete'

    def __init__(self, method):
        if method not in {self.GET, self.PUT, self.POST, self.PATCH, self.DELETE}:
            raise UnsupportedMethodError('"%s" is not supported!' % method)

        self._method = method

    @property
    def method(self):
        return self._method


class UnsupportedMethodError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
