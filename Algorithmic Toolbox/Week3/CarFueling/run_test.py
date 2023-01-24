import sys
from naive_car_fueling import naive_car_fueling
from car_fueling import car_fueling
import time
import random

if __name__ == '__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    manual_tests = {(950, 400, 4,(200, 375, 550, 750)): 2,
                    (10, 3, 4,(1, 2, 5, 9)): -1,
                    (200, 250, 2,(100,150)): 0}


    if (test_case == 'test_model'):
        # Verify naive solution with answers worked out
        # on paper.
        for n in list(manual_tests.keys()):
            print(f'd: {n[0]}\tm: {n[1]}\tn: {n[2]}')
            print(n[3])
            naive_soln_ans = naive_car_fueling(*n)
            print(naive_soln_ans,manual_tests[n])
            assert(naive_soln_ans == manual_tests[n])

    elif (test_case == 'manual'):
        # Verify efficient solution with answers worked
        # out on paper.
        for n in list(manual_tests.keys()):
            print(f'd: {n[0]}\tm: {n[1]}\tn: {n[2]}')
            print(n[3])
            efficient_soln_ans = car_fueling(n[0],n[1],n[2],list(n[3]))
            print(efficient_soln_ans,manual_tests[n])
            assert(efficient_soln_ans == manual_tests[n])
            
    elif (test_case == 'time'):
        python_time_constraint = 5.0
        worst_case_d = 10**5
        worst_case_m = 400
        worst_case_n = worst_case_d//400 - 1
        worst_case_stops = list(range(400,worst_case_d,400))
        
        start = time.process_time()
        print(car_fueling(worst_case_d, worst_case_m, worst_case_n, worst_case_stops))
        end = time.process_time()
        print(f'Process time: {end-start} s')
        assert((end-start) <= python_time_constraint)

    elif (test_case == 'stress'):
        for i in range(num_tests):
            d = random.randint(1,100)
            m = random.randint(1,10)
            n = random.randint(1,15)
            stops = [0]*n # Init stops
            stops[0] = random.randint(1,m)
            for j in range(1,n):
                stops[j] = stops[j-1] + random.randint(1,m)
                if stops[j] >= d:
                    n = j # 1 less
                    stops = stops[:j]
                    break
            print(f'd: {d}\tm: {m}\tn: {n}')
            print(stops)
            naive_soln_ans = naive_car_fueling(d,m,n,stops)
            efficient_soln_ans = car_fueling(d,m,n,stops)
            print(naive_soln_ans, efficient_soln_ans)
            assert(efficient_soln_ans == naive_soln_ans)
            
    else:
        raise Exception('Unrecognised test case specified.')
