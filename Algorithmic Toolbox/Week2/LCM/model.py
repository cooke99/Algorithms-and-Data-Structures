import time

def naive_LCM(a: int, b: int) -> int:
    # Naive algo to find the LCM of 2 ints a and b.
    for i in range(max(a,b), (a*b)+1):
        # LCM can not be smaller than max(a,b)
        # and cannot be larger than a*b.
        if ((i%a == 0) and (i%b==0)):
            return i
        
if __name__ == '__main__':
    inputs = list(map(int,input().split()))
    a = inputs[0]
    b = inputs[1]
    start = time.process_time()
    ans = naive_LCM(a, b)
    end = time.process_time()
    print(ans)
    print(f'Runtime: {end-start} s')
    
