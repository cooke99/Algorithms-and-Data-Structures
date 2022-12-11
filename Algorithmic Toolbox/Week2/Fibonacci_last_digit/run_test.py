import sys
from efficient_fibonacci_last_digit import efficient_fibonacci_last_digit
from model import naive_fib_last_digit
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {0:0,
                    1:1,
                    2:1,
                    3:2,
                    4:3,
                    5:5,
                    6:8,
                    7:3,
                    8:1,
                    9:4,
                    10:5,
                    11:9,
                    12:4,
                    13:3,
                    100:5,
                    139:1,
                    91239:6}

    if (test_case == 'test_model'):
        # Verify solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(n)
            naive_soln_ans = naive_fib_last_digit(n)
            print(naive_soln_ans,manual_tests[n])
            assert(naive_soln_ans == manual_tests[n])

    elif (test_case == 'manual'):
        # Verify solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(n)
            efficient_soln_ans = efficient_fibonacci_last_digit(n)
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans == manual_tests[n])

    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_input = 10**6
        start = time.process_time()
        _ = efficient_fibonacci_last_digit(worst_case_input)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            n = random.randint(0,10**5) # Limited range for speed.
            print(n)
            efficient_soln_ans = efficient_fibonacci_last_digit(n)
            naive_soln_ans = naive_fib_last_digit(n)
            print(efficient_soln_ans, naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
    else:
        raise Exception('Unrecognised test case specified.')
