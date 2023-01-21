import time

def naive_last_digit_sum_fibonacci(n: int) -> int:
    # Return last digit of sum of Fibonacci
    # numbers up to Fn.
    if (n <= 1):
        return n

    else:
        Fn = [0]*(3) # Create an array initialised with zeros of size 3 (accomodate large range of n).
        # Simple cases
        Fn[0] = 0
        Fn[1] = 1
        _sum = 1 # Initialise sum
        for i in range(2,n+1):
            Fn[i%3] = (Fn[(i-1)%3] + Fn[(i-2)%3])%10
            _sum = (_sum + Fn[i%3])%10
        return _sum

if __name__ == '__main__':
    n = int(input())
    start = time.process_time()
    ans = naive_last_digit_sum_fibonacci(n)
    end = time.process_time()
    print(ans)
    print(f'Runtime: {end-start} s')
