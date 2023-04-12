from math import sqrt
import numpy as np
# We seed the cache with the first two odd primes because (1) it's low-
# hanging fruit and (2) we avoid the need to add extra lines of code (that
# will increase execution time) for cases in which the square roots of numbers
# are less than any primes in the list
odd_primes = [2, 3, 5]


# def is_prime(n):

#     # If n is not prime, it must have at least one factor less than its square
#     # root.
#     max_prime_factor_limit = int(sqrt(n))

#     # use a generator here to avoid evaluating all the qualifying values in
#     # odd_primes until you need them. For example, the square root of 27 is
#     # 5.1962, but, since it's divisible by 3, you'll only test if 27 is prime
#     # one time. Not a big deal with smaller integers, but the time to compute
#     # the next prime will increase pretty fast as there are more potential
#     # factors.

#     available_primes = (p for p in odd_primes if p <= max_prime_factor_limit)

#     for prime in available_primes:
#         if n % prime == 0:
#             return False

#     return True

def primeFactorization(n):
    '''
        this is a utility function used to attack the RSA algorithm using the prime factorization attack
    '''
    # since the maximum factor must be less than the square root of n
    max_factor = int(np.ceil(np.sqrt(n)))
    primeFactors = []
    divisior = 2
    while divisior <= n:
        if n % divisior == 0:
            primeFactors.append(divisior)
            n = n/divisior
        else:
            divisior += 1

    return primeFactors
