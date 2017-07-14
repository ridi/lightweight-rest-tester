import unittest


from rest_tester.function.fail import FailTestFunction


class TestFailTestFunction(unittest.TestCase):
    def test_generate_name(self):
        file_name = 'file_name'

        actual = FailTestFunction.generate_name(file_name)
        expected = 'test_%s' % file_name

        self.assertEqual(actual, expected)

    def test_make(self):
        try:
            test_function = FailTestFunction.make('test_function')
            test_function(self)
            self.fail('Should throw AssertionError!')
        except AssertionError:
            pass

if __name__ == '__main__':
    unittest.main()
