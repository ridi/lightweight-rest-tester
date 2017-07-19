import unittest


from rest_tester.function.fail import FailTestFunctionBuilder


class TestFailTestFunction(unittest.TestCase):
    def test_build(self):
        builder = FailTestFunctionBuilder('Throw AssertionError!', 'fail test case')
        fail_function = builder.build()

        try:
            fail_function.test_function(self)
            self.fail('Should throw AssertionError!')
        except AssertionError:
            pass

if __name__ == '__main__':
    unittest.main()
