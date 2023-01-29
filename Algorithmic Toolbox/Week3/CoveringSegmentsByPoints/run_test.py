import sys
from naive_covering_segments import naive_covering_segments
from covering_segments import covering_segments
import time
import random
import numpy as np

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(5, (0,1,4,6,7),(2,4,7,9,10)): 2,
                    (5, (0,40,55,15,70), (15,70,80,30,100)): 2,
                    (1, (2,),(3,)): 1,
                    (3,(1,2,3),(3,5,6)):1,
                    (4,(4,1,2,5),(7,3,5,6)):2}
    manual_tests_naive = {(5, (0,1,4,6,7),(2,4,7,9,10)): 2,
                    (1, (2,),(3,)): 1,
                    (3,(1,2,3),(3,5,6)):1,
                    (4,(4,1,2,5),(7,3,5,6)):2}

    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n in list(manual_tests_naive.keys()):
            print(f'n: {n[0]}')
            print(n[1])
            print(n[2])
            naive_soln_ans = naive_covering_segments(*n)
            print(naive_soln_ans,manual_tests_naive[n])
            assert(naive_soln_ans[0] == manual_tests_naive[n])

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n[0]}')
            print(n[1])
            print(n[2])
            efficient_soln_ans = covering_segments(n[0],np.array(n[1]),np.array(n[2]))
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans[0] == manual_tests[n])
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_n = 100
        worst_case_L = [i*10**7 for i in range(worst_case_n)]
        worst_case_R = [i*10**7 for i in range(1,worst_case_n+1)]
        
        start = time.process_time()
        print(covering_segments(worst_case_n, np.array(worst_case_L), np.array(worst_case_R)))
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            n = random.randint(1,10)
            L = [random.randint(0,10) for i in range(n)]
            R = [L[j]+random.randint(0,10) for j in range(n)]
            print(f'n: {n}')
            print(L)
            print(R)
            naive_soln_ans = naive_covering_segments(n,L,R)
            efficient_soln_ans = covering_segments(n,np.array(L),np.array(R))
            print(naive_soln_ans, efficient_soln_ans)
            assert(efficient_soln_ans[0] == naive_soln_ans[0])
            
    else:
        raise Exception('Unrecognised test case specified.')
