import sys
from naive_fractional_knapsack import naive_fractional_knapsack
from fractional_knapsack import fractional_knapsack
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(3, 9,(5000,200,10),(4,3,5)): 5204.0,
                    (3, 50,(60,100,120),(20,50,30)): 180.0,
                    (1, 10,(500,),(30,)): 500/3}


    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n[0]}\tW: {n[1]}')
            for i in range(n[0]):
                print(n[2][i],n[3][i])
            naive_soln_ans = naive_fractional_knapsack(*n)
            print(naive_soln_ans,manual_tests[n])
            assert(abs(naive_soln_ans - manual_tests[n])<1e-4)

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n[0]}\tW: {n[1]}')
            for i in range(n[0]):
                print(n[2][i],n[3][i])
            efficient_soln_ans = fractional_knapsack(n[0],n[1],list(n[2]),list(n[3]))
            print(efficient_soln_ans,manual_tests[n])
            assert(abs(efficient_soln_ans - manual_tests[n])<1e-4)
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_n = 1000
        worst_case_W = 2*(10**6)
        worst_case_costs = [2*(10**6)]*worst_case_n
        worst_case_weights = [1]*worst_case_n
        
        start = time.process_time()
        _ = fractional_knapsack(worst_case_n, worst_case_W, worst_case_costs, worst_case_weights)
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            n = random.randint(1,10)
            W = random.randint(0,100)
            costs = [random.randint(0,500) for j in range(n)]
            weights = [random.randint(1,10) for j in range(n)]
            print(f'n: {n}\tW: {W}')
            print(costs)
            print(weights)
            naive_soln_ans = naive_fractional_knapsack(n,W,costs,weights)
            efficient_soln_ans = fractional_knapsack(n,W,costs,weights)
            print(naive_soln_ans, efficient_soln_ans)
            assert(abs(efficient_soln_ans - naive_soln_ans)<1e-4)
            
    else:
        raise Exception('Unrecognised test case specified.')
