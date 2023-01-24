import sys
from naive_dot_product import naive_dot_product
from dot_product import dot_product
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(4, (1,2,3,4),(1,2,3,4)): 30,
                    (1, (2,), (2,)): 4,
                    (6, (1,2,3,4,5,6),(1,2,3,4,5,6)): 91,
                    (3,(0,0,0),(0,0,0)):0,
                    (1,(23,),(39,)):897,
                    (3,(2,3,9),(7,4,2)):79}


    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n[0]}')
            print(n[1])
            print(n[2])
            naive_soln_ans = naive_dot_product(*n)
            print(naive_soln_ans,manual_tests[n])
            assert(naive_soln_ans == manual_tests[n])

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n in list(manual_tests.keys()):
            print(f'n: {n[0]}')
            print(n[1])
            print(n[2])
            efficient_soln_ans = dot_product(n[0],list(n[1]),list(n[2]))
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans == manual_tests[n])
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_n = 10**3
        worst_case_prices = [10**5]*worst_case_n
        worst_case_clicks = [10**5]*worst_case_n
        
        start = time.process_time()
        print(dot_product(worst_case_n, worst_case_prices, worst_case_clicks))
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            n = random.randint(1,10)
            prices = [random.randint(0,10**5) for i in range(n)]
            clicks = [random.randint(0,10**5) for i in range(n)]
            print(f'n: {n}')
            print(prices)
            print(clicks)
            naive_soln_ans = naive_dot_product(n,prices,clicks)
            efficient_soln_ans = dot_product(n,prices,clicks)
            print(naive_soln_ans, efficient_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
            
    else:
        raise Exception('Unrecognised test case specified.')
