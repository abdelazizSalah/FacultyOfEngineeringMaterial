from math import sqrt
import numpy as np
import rsa


def primeFactorization(n):
    '''
        this is a utility function used to attack the RSA algorithm using the prime factorization attack
    '''
    # since the maximum factor must be less than the square root of n
    max_factor = int(np.ceil(np.sqrt(n)))
    primeFactors = []
    divisior = 2
    while divisior <= max_factor:
        if n % divisior == 0:
            primeFactors.append(divisior)
            n = n/divisior
        else:
            divisior += 1

    return primeFactors


print(primeFactorization(9))
