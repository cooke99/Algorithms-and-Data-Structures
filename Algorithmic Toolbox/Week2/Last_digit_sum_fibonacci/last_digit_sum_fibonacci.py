import time

def efficient_fibonacci_mod_m(n: int, m: int) -> int:
    # Return nth Fibonacci number modulo m
    if (n <= 1):
        # m >= 2 by definition.
        return n

    else:
        # Exploit periodicity of Fn mod m to efficiently obtain an answer.
        Fn = [0,1,0] # Create an array initialised with first 2 elements of Fn.
        i = 2
        Fn[i%3] = (Fn[(i-1)%3] + Fn[(i-2)%3])%m
        while (i != (n+1)) and (Fn[i%3] != 0):
            # Calculate Fn mod m until either a) we reach Fn or b) we find
            # the restricted period of Fn mod m.
            i += 1
            Fn[i%3] = (Fn[(i-1)%3] + Fn[(i-2)%3])%m
            

        if (i == (n+1)):
            # If a) from above is met.
            return Fn[n%3]

        else:
            # If b) from above is met.
            restricted_period = i # Index of first Fibonacci element divisible by m.
            i += 1
            multiplier = Fn[i%3] = (Fn[(i-1)%3] + Fn[(i-2)%3])%m # The first residue after the restricted period is the multiplier.
            # We don't need any more elements from the sequence once we've found the multiplier
            # and restricted period.
            order = 1 # We need to find the order of the multiplier
            # i.e. the least positive integer n such that multiplier^n ≡ 1 (mod m).
            while (((multiplier**order)% m) != 1):
                # Use a simple while loop.
                # It has been proven that the order can only be 1, 2, or 4.
                order += 1
            period = order*restricted_period # The length of the cyclic period of Fib(n) mod m.
            if (n%period) <= 1:
                return n%period
            else:
                # We have to recalculate the Fibonacci sequence as the previous
                # Fn only stores past 3 elements of sequence (to meet memory requirements
                # if n is big).
                Fn = [0,1,0] # Create an array initialised with first 2 elements of Fn.
                for j in range(2,(n%period)+1):
                    Fn[j%3] = (Fn[(j-1)%3] + Fn[(j-2)%3])%m
                return Fn[j%3]

def last_digit_sum_fibonacci(n: int) -> int:
    # Using small values of n, worked out
    # formula for last digit of sum of fibonacci
    # numbers:
    if (n <= 1):
        return n
    else:
        ans = efficient_fibonacci_mod_m(n + 2, 10)
        if (ans == 0):
            # The correct order of operations should be
            # (F(n+2) - 1)%10. But using efficient_fibonacci_mod_m,
            # we have to do F(n+2)%10 - 1.
            # These expressions are equivalent for all cases except
            # where F(n+2)%10 == 0. Therefore, this if statement
            # handles this case (ans can only be 0 for Fn%10 == 0
            # as we are handling the case of n = 0 above).
            return 9
        else:
            return ans - 1 

if __name__ == '__main__':
    n = int(input())
    ans = last_digit_sum_fibonacci(n)
    print(ans)
