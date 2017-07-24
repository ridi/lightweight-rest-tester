import time


def run_test_function_list(test_function_list, test_self):
    time.sleep(1)

    for test_function in test_function_list:
        test_function.test_function(test_self)
