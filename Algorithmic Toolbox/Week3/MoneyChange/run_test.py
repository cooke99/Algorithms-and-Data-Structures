import sys
from naive_change_money import naive_change_money
from efficient_change_money import efficient_change_money
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {28:6,
                    51:6,
                    79:12,
                    116:13,
                    222:24,
                    679:72,
                    838:87,
                    999:104}

    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(f'money: {n}')
            naive_soln_ans = naive_change_money(n)
            print(naive_soln_ans,manual_tests[n])
            assert(naive_soln_ans == manual_tests[n])

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n in list(manual_tests.keys()):
            print(f'money: {n}')
            efficient_soln_ans = efficient_change_money(n)
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans == manual_tests[n])
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_n = 999
        start = time.process_time()
        _ = efficient_change_money(worst_case_n)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for n in range(1,1001):
            print(f'money: {n}')
            efficient_soln_ans = efficient_change_money(n)
            naive_soln_ans = naive_change_money(n)
            print(efficient_soln_ans, naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
            
    else:
        raise Exception('Unrecognised test case specified.')
