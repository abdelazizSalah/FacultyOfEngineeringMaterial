# Large Prime Generation for RSA
import random

if __name__ == '__main__':
    while True:
        n = 50
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            print(n, "bit prime is: \n", prime_candidate)
            break
