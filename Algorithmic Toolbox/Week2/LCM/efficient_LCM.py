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

def LCM(a: int, b: int) -> int:
    # LCM of 2 numbers can be found by dividing 
    # their product by their GCD. Proof in repo.
    return (a*b)//EuclidGCD(a,b)
       
if __name__ == '__main__':
    a,b = list(map(int,input().split()))
    print(LCM(a, b))
