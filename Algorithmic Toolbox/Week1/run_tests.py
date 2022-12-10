import sys
import time
from maximum_pairwise_product import *
import random

def generate_manual_tests():
    n = [2*(10**5),2*(10**5),2,2,5,5,5,5,5]
    arr = [[2*(10**5)]*n[0],
           [0]*n[1],
           [2*(10**5)]*n[2],
           [0]*n[3],
           [5,4,3,2,1],
           [1,2,3,4,5],
           [5,1,4,3,5],
           [2,1,4,1,3],
           [2,3,1,1,1]]
    labels = [(2*(10**5))**2,
              0,
              (2*(10**5))**2,
              0,
              20,
              20,
              25,
              12,
              6]

    return n, arr, labels

def model(n: int, arr: list):
    max_prod = -1

    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]*arr[j] > max_prod):
                max_prod = arr[i]*arr[j]

    return max_prod

def stress_test(n: int):
    # Do not set seed or it will sample same numbers every time.
    arr = random.choices(list(range(n)), k = n)
    return arr
    

if __name__=='__main__':
    test_case = str(sys.argv[1])
    num_tests = int(sys.argv[2])
    n = int(sys.argv[3])

    if (test_case == 'manual'):
        n, arr, labels = generate_manual_tests()
        for i in range(len(n)):
            print(maximum_pairwise_product(n[i],arr[i]),labels[i])
            # Check functionality:
            assert(maximum_pairwise_product(n[i],arr[i])==labels[i])
            #Check clock time:
            start = time.time()
            maximum_pairwise_product(n[i],arr[i])
            end = time.time()
            assert((end-start)<= 1)

    elif (test_case == 'model'):
        n, arr, labels = generate_manual_tests()
        for i in range(2,len(n)):
            print(model(n[i],arr[i]),labels[i])
            # Check functionality:
            assert(model(n[i],arr[i])==labels[i])

    else:
        # stress test
        for i in range(num_tests):
            arr = stress_test(n)
            print(arr)
            print(model(n,arr),maximum_pairwise_product(n,arr))
            # Check functionality:
            assert(model(n,arr)==maximum_pairwise_product(n,arr))
            
            
