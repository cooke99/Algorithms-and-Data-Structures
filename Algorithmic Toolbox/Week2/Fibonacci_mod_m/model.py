import time

def naive_fibonacci_mod_m(n: int, m: int) -> int:
    # Return nth Fibonacci number modulo m
    # O(n^2)
    if (n <= 1):
        return n

    else:
        Fn = [0]*(3) # Create an array initialised with zeros of size 3 (accomodate large range of n).
        # Simple cases
        Fn[0] = 0
        Fn[1] = 1
        for i in range(2,n+1):
            Fn[i%3] = (Fn[(i-1)%3] + Fn[(i-2)%3])%m
        return Fn[i%3]

if __name__ == '__main__':
    inputs = list(map(int,input().split()))
    n = inputs[0]
    m = inputs[1]
    start = time.process_time()
    ans = naive_fibonacci_mod_m(n, m)
    end = time.process_time()
    print(ans)
    print(f'Runtime: {end-start} s')
