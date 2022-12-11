from efficient_fibonacci import efficient_fibonacci

def naive_fib_last_digit(n: int) -> int:
    return int(str(efficient_fibonacci(n))[-1])

if __name__ == '__main__':
    n = int(input())
    print(naive_fib_last_digit(n))
