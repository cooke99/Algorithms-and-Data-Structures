import time

def naive_GCD(a: int, b: int) -> int:
    # Naive algo to find the GCD of 2 ints a and b.
    smaller = min(a,b) # GCD can not be bigger than the smaller of a and b
    for i in range(smaller, 0, -1):
        # Start from smallest number and work backwards to find GCD.
        if ((a%i == 0) and (b%i==0)):
            return i
        
if __name__ == '__main__':
    inputs = list(map(int,input().split()))
    a = inputs[0]
    b = inputs[1]
    start = time.process_time()
    ans = naive_GCD(a, b)
    end = time.process_time()
    print(ans)
    print(f'Runtime: {end-start} s')
    
