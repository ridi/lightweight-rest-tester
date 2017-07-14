class FailTestFunction(object):
    @staticmethod
    def generate_name(file_name):
        """Test function name should start with 'test' since we use unit test."""
        return 'test_%s' % file_name

    @staticmethod
    def make(msg):
        """Make a test function"""

        def test_fail(self):
            self.fail(msg)

        return test_fail
