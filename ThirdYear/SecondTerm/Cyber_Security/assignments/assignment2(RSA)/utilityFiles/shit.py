from math import sqrt, ceil
import numpy as np
import socket
import time
'''
    Attack file:
        here we want to apply the attack
        so the algorithm will be as follows:
            1- read the public key of the server
            2- apply prime factorization on n
            3- calculate phi(n)
            4- calculate d
            5- decrypt the message
'''


def primeFactorization(n):
    '''
        this is a utility function used to attack the RSA algorithm using the prime factorization attack
    '''
    # since the maximum factor must be less than the square root of n
    max_factor = int(ceil(sqrt(n)))
    print(max_factor)
    primeFactors = []
    divisior = 2
    while divisior <= max_factor:
        if n % divisior == 0:
            primeFactors.append(divisior)
            n = n/divisior
        else:
            divisior += 1

    return primeFactors
