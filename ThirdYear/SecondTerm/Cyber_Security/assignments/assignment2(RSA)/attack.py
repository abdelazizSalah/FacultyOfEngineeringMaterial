from math import sqrt
import numpy as np
import socket
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


# the used format.
FORMAT = 'utf-8'
# condition of closing
DISCONECTIONCONDITION = 'DES'
# Header
HEADER = 64

# here, the server must be fixed
SERVER = '127.0.0.1'
# the port on which we are connected
PORT = 5050
# define ADDR
ADDR = (SERVER, PORT)
# define client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# make the connection on certain address
client.connect(ADDR)


#################!     Applying the attack     !#################
# 1. read the public key
msg_len = client.recv(HEADER).decode(FORMAT)
e = client.recv(int(msg_len)).decode(FORMAT)
e = int(e)
msg_len = client.recv(HEADER).decode(FORMAT)
n = client.recv(int(msg_len)).decode(FORMAT)
n = int(n)
PublicKey = (e, n)

print(f'PublicKey = {PublicKey}', flush=True)
# 2. apply prime factorization on n
primeFactors = primeFactorization(n)

# 3. calculate phi(n)
phi_n = (primeFactors[0] - 1) * \
    ((np.divide(PublicKey[1], primeFactors[0])) - 1)

phi_n = int(phi_n)
# 4. calculate d
d = pow(PublicKey[0], -1, phi_n)

print(
    'private key is ', (d, PublicKey[1])
)
