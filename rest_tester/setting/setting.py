from .target import TestTarget
from rest_tester.utils import convert_to_list


class TestSetting(object):
    def __init__(self, json_data, options):
        self._targets = []
        for json_target in convert_to_list(json_data):
            self._targets.append(TestTarget(json_target, options))

    @property
    def targets(self):
        return self._targets

    def has_multiple_targets(self):
        return len(self._targets) > 1
