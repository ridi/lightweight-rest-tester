import unittest


from rest_tester.function.fail import FailTestFunctionBuilder


class TestFailTestFunction(unittest.TestCase):
    def test_build(self):
        builder = FailTestFunctionBuilder('Throw AssertionError!', 'fail test case')
        fail_function = builder.build()

        with self.assertRaises(AssertionError):
            fail_function.test_function(self)

if __name__ == '__main__':
    unittest.main()
