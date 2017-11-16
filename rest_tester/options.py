from .utils import read_json_file


class AuthenticationError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Options(object):
    def __init__(self, base_url=None, auth_file=None):
        self._base_url = base_url
        self._auth = self._read_authentication(auth_file)

    @staticmethod
    def _read_authentication(auth_file):
        if auth_file is not None:
            try:
                auth_json = read_json_file(auth_file)
            except FileNotFoundError:
                print('Cannot find authentication file. So, we do not use authentication.')
                return None

            try:
                return auth_json['user'], auth_json['pass']
            except KeyError:
                raise AuthenticationError('Authentication information format is wrong.')

        return None

    @property
    def base_url(self):
        return self._base_url

    @property
    def auth(self):
        return self._auth
