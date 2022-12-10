def recursive_fibonacci(n: int) -> int:
    # Return nth Fibonacci number
    if (n <= 1):
        # Base case
        return n
    else:
        # Recursive case
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

if __name__ == '__main__':
    n = int(input())
    print(recursive_fibonacci(n))
