import sys
from efficient_fibonacci_mod_m import efficient_fibonacci_mod_m
from model import naive_fibonacci_mod_m
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(1,2):1,
                    (1,1000):1,
                    (1,3):1,
                    (2,3):1,
                    (3,3):2,
                    (4,3):0,
                    (5,3):2,
                    (6,3):2,
                    (7,3):1,
                    (8,3):0,
                    (9,3):1,
                    (10,3):1,
                    (11,3):2,
                    (12,3):0,
                    (13,3):2,
                    (14,3):2,
                    (15,3):1,
                    (1,5):1,
                    (2,5):1,
                    (3,5):2,
                    (4,5):3,
                    (5,5):0,
                    (6,5):3,
                    (7,5):3,
                    (8,5):1,
                    (9,5):4,
                    (10,5):0,
                    (11,5):4,
                    (12,5):4,
                    (13,5):3,
                    (14,5):2,
                    (15,5):0,
                    (1,4):1,
                    (2,4):1,
                    (3,4):2,
                    (4,4):3,
                    (5,4):1,
                    (6,4):0,
                    (7,4):1,
                    (8,4):1,
                    (9,4):2,
                    (10,4):3,
                    (11,4):1,
                    (12,4):0,
                    (13,4):1,
                    (14,4):1,
                    (15,4):2,
                    (1,239):1,
                    (115,1000):885}      

    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n,m in list(manual_tests.keys()):
            print(f'n: {n}\tm:{m}')
            naive_soln_ans = naive_fibonacci_mod_m(n,m)
            print(naive_soln_ans,manual_tests[(n,m)])
            assert(naive_soln_ans == manual_tests[(n,m)])

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n,m in list(manual_tests.keys()):
            print(f'n: {n}\tm:{m}')
            efficient_soln_ans = efficient_fibonacci_mod_m(n,m)
            print(efficient_soln_ans,manual_tests[(n,m)])
            assert(efficient_soln_ans == manual_tests[(n,m)])
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_n = 10**14
        worst_case_m = 1000
        start = time.process_time()
        _ = efficient_fibonacci_mod_m(worst_case_n, worst_case_m)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            n = random.randint(1,10**7) # Limited range for speed.
            m = random.randint(2,10**3)
            print(f'n: {n}\tm:{m}')
            efficient_soln_ans = efficient_fibonacci_mod_m(n,m)
            naive_soln_ans = naive_fibonacci_mod_m(n,m)
            print(efficient_soln_ans, naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
            
    else:
        raise Exception('Unrecognised test case specified.')
