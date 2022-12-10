def efficient_fibonacci(n: int) -> int:
    # Return nth Fibonacci number (efficient-er, still O(n^2))
    if (n <= 1):
        return n

    else:
        Fn = [0]*(n+1) # Create an array initialised with zeros of size n.
        # Simple cases
        Fn[0] = 0
        Fn[1] = 1
        for i in range(2,n+1):
            Fn[i] = Fn[i-1] + Fn[i-2]
        return Fn[-1]
    

if __name__ == '__main__':
    n = int(input())
    print(efficient_fibonacci(n))
