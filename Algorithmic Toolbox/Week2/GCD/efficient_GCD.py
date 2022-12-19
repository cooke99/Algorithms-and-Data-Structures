def EuclidGCD(a: int, b: int) -> int:
    # Efficient algo to find the GCD of 2 ints a and b.
    # Uses Euclid's algorithm which states that the GCD
    # of 2 numbers a and b is equivalent to the GCD of
    # a%b and b.
    if (b == 0):
        # If b is 0, then a was divisible by b at previous iteration.
        return a
    else:
        a_prime = a % b
        return EuclidGCD(b,a_prime)
    
        
if __name__ == '__main__':
    a,b = list(map(int,input().split()))
    print(EuclidGCD(a, b))
