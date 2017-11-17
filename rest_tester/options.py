class AuthenticationError(Exception):
    """Wrongly defined authentication information"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Options(object):
    def __init__(self, base_url=None, auth=None):
        self._base_url = base_url
        self._auth = self._read_authentication(auth)

    @staticmethod
    def _read_authentication(auth):
        if auth is not None:
            auth_decomp = auth.split(':')
            if len(auth_decomp) != 2:
                raise AuthenticationError('Authentication information is wrong.')

            return auth_decomp[0], auth_decomp[1]

        return None

    @property
    def base_url(self):
        return self._base_url

    @property
    def auth(self):
        return self._auth
