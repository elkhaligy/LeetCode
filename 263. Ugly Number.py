import math

def get_factors(n: int):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: # n = i * k (i is a factor, also k is a factor)
            factors.add(i) 
            factors.add(n // i)
    return factors

def is_prime(n):
    prime_flag = 0
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_flag = 1
            break

    if prime_flag == 0:
        return True
    else:
        return False

def isUgly(n: int) -> bool:
    factors = get_factors(n)
    prime_factors = set()
    for factor in factors:
        if is_prime(factor):
            prime_factors.add(factor)
    print(prime_factors)
    if len(prime_factors) == 0:
        return True
    # if any number of the prime_factors is anything other than 2, 3 or 5 return false
    for factor in prime_factors:
        if factor != 2 and factor != 3 and factor != 5:
            return False
    return True

print(is_prime(8))