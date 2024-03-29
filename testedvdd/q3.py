import math
n = 600851475143
def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True
def prime_factors(n):
    factors = []
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(i):
            if n % i == 0:
                factors.append(i)
                pair = n / i
                if is_prime(pair):
                    factors.append(pair)
    return sorted(factors)
l = prime_factors(n)

print(l[-1])