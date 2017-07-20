import unittest


from rest_tester.function.fail import FailTestFunctionBuilder


class TestFailTestFunction(unittest.TestCase):
    def test_build(self):
        builder = FailTestFunctionBuilder('Throw AssertionError!', 'fail test case')
        fail_function = builder.build()

        try:
            fail_function.test_function(self)
        except AssertionError:
            pass
        else:
            self.fail('Should throw AssertionError!')

if __name__ == '__main__':
    unittest.main()
