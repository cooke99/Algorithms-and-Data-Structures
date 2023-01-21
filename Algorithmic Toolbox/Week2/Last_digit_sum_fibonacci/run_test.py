import sys
from last_digit_sum_fibonacci import *
from model import naive_last_digit_sum_fibonacci
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {0:0,
                    1:1,
                    2:2,
                    3:4,
                    4:7,
                    5:2,
                    6:0,
                    7:3,
                    8:4,
                    9:8,
                    10:3,
                    11:2,
                    12:6,
                    100:5}

    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n}')
            naive_soln_ans = naive_last_digit_sum_fibonacci(n)
            print(naive_soln_ans,manual_tests[n])
            assert(naive_soln_ans == manual_tests[n])

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n}')
            efficient_soln_ans = last_digit_sum_fibonacci(n)
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans == manual_tests[n])
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_n = 10**14
        start = time.process_time()
        _ = last_digit_sum_fibonacci(worst_case_n)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            n = random.randint(0,10**6) # Limited range for speed.
            print(f'n: {n}')
            efficient_soln_ans = last_digit_sum_fibonacci(n)
            naive_soln_ans = naive_last_digit_sum_fibonacci(n)
            print(efficient_soln_ans, naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
            
    else:
        raise Exception('Unrecognised test case specified.')
