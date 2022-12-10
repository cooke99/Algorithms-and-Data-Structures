import sys
from model import recursive_fibonacci
from efficient_fibonacci import efficient_fibonacci
import time

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    manual_tests = {0:0,
                    1:1,
                    2:1,
                    3:2,
                    4:3,
                    5:5,
                    6:8,
                    7:13,
                    8:21,
                    9:34,
                    10:55,
                    11:89,
                    12:144}

    if (test_case == 'test_model'):
        # Verify solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(n)
            naive_soln_ans = recursive_fibonacci(n)
            print(naive_soln_ans,manual_tests[n])
            assert(naive_soln_ans == manual_tests[n])

    elif (test_case == 'manual'):
        # Verify solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(n)
            efficient_soln_ans = efficient_fibonacci(n)
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans == manual_tests[n])

    elif(test_case == 'constraint_range'):
        # Input range limited to 0 <= n <= 45
        # This test tests over this entire range.
        for n in range(0,46):
            print(n)
            efficient_soln_ans = efficient_fibonacci(n)
            naive_soln_ans = recursive_fibonacci(n)
            print(efficient_soln_ans,naive_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)

    elif(test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_input = 45
        start = time.process_time()
        _ = efficient_fibonacci(worst_case_input)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    else:
        raise Exception('Unrecognised test case specified.')
