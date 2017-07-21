import unittest
import os


from rest_tester.main import main


class TestMain(unittest.TestCase):
    current_dir_path = os.path.dirname(__file__)

    def test_main(self):
        script = ''
        test_suites_dir = '%s/resources/' % self.current_dir_path

        main((script, test_suites_dir))

    def test_invalid_arguments(self):
        argv = ''

        try:
            main(argv)
        except ValueError:
            pass
        else:
            self.fail('Should thrown ValueError!')

if __name__ == '__main__':
    unittest.main()
