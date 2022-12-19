import sys
from model import naive_GCD
from efficient_GCD import EuclidGCD
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(14,12):2,
                    (30,19):1,
                    (66,100):2,
                    (28851538,1183019):17657,
                    (1,1):1,
                    (2,2):2,
                    (2*10**9,2*10**9):2*10**9}

    if (test_case == 'test_model'):
        # Verify solution with answers worked out
        # on paper.
        for inputs in list(manual_tests.keys()):
            print(inputs)
            naive_soln_ans = naive_GCD(inputs[0],inputs[1])
            print(naive_soln_ans,manual_tests[inputs])
            assert(naive_soln_ans == manual_tests[inputs])

    elif (test_case == 'manual'):
        # Verify solution with answers worked out
        # on paper.
        for inputs in list(manual_tests.keys()):
            print(inputs)
            efficient_soln_ans = EuclidGCD(inputs[0],inputs[1])
            print(efficient_soln_ans,manual_tests[inputs])
            assert(efficient_soln_ans == manual_tests[inputs])

    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_input = 2*10**9
        start = time.process_time()
        _ = EuclidGCD(worst_case_input, worst_case_input-1)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            a = random.randint(1,10**7) # Limited range for speed.
            b = random.randint(1,10**7)
            print(a,b)
            efficient_soln_ans = EuclidGCD(a,b)
            naive_soln_ans = naive_GCD(a,b)
            print(efficient_soln_ans, naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
    else:
        raise Exception('Unrecognised test case specified.')
