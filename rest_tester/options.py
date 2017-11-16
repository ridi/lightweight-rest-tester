class AuthenticationError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


def _read_authentication_password_file(file_path):
    with open(file=file_path) as file:
        return file.read().splitlines()[0]


class Options(object):
    def __init__(self, base_url=None, auth_user=None, auth_pass_file=None):
        self._base_url = base_url

        if auth_user and auth_pass_file:
            try:
                auth_pass = _read_authentication_password_file(auth_pass_file)
            except:
                raise AuthenticationError('Authentication information is given, but password file is missing!')

            self._auth = (auth_user, auth_pass)
        else:
            self._auth = None

    @property
    def base_url(self):
        return self._base_url

    @property
    def auth(self):
        return self._auth
