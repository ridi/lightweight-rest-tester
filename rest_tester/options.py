class Options(object):
    def __init__(self, base_url=None):
        self._base_url = base_url

    @property
    def base_url(self):
        return self._base_url
