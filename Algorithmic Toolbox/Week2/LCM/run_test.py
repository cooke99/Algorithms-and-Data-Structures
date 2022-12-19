import sys
from model import naive_LCM
from efficient_LCM import *
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(8,6):24,
                    (6,15):30,
                    (8,15):120,
                    (2,3):6,
                    (7,8):56,
                    (761457,614573):467970912861}

    if (test_case == 'test_model'):
        # Verify naive solution with
        # answers worked out on paper.
        for inputs in list(manual_tests.keys()):
            print(inputs)
            naive_soln_ans = naive_LCM(inputs[0],inputs[1])
            print(naive_soln_ans,manual_tests[inputs])
            assert(naive_soln_ans == manual_tests[inputs])

    elif (test_case == 'manual'):
        # Verify efficient solution 
        # with answers worked out on paper.
        for inputs in list(manual_tests.keys()):
            print(inputs)
            efficient_soln_ans = LCM(inputs[0],inputs[1])
            print(efficient_soln_ans,manual_tests[inputs])
            assert(efficient_soln_ans == manual_tests[inputs])

    elif (test_case == 'time'):
        # Time constraint test
        python_time_constraint = 5.0 # 5 s limit placed by coursera.
        worst_case_input = 10**7 # Worst case input deemed to be largest numbers.
        start = time.process_time()
        _ = LCM(worst_case_input, worst_case_input-1)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        # Stress test involves generating random
        # inputs, from which the outputs of the naive
        # and efficient solution can be compared.
        for i in range(num_tests):
            a = random.randint(1,10**4) # Limited range for speed.
            b = random.randint(1,10**4)
            print(a,b)
            efficient_soln_ans = LCM(a,b)
            naive_soln_ans = naive_LCM(a,b)
            print(efficient_soln_ans, naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
    else:
        raise Exception('Unrecognised test case specified.')
