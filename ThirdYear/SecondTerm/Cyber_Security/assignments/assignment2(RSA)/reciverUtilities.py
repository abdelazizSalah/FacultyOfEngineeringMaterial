import numpy as np
import socket
import time
import random
from math import sqrt, ceil, gcd

# the used format.
FORMAT = 'utf-8'
# condition of closing
DISCONECTIONCONDITION = 'DES'
# Header
HEADER = 64


def getPlainTextAfterDecryption(num, conversionMap):
    '''
        this is a utility function used to return the decrypted message from the number
        into the original plain text
    '''
    message = []
    # this to reverse the mapping. so we can get the character from the number
    newMap = {v: k for k, v in conversionMap.items()}
    for i in range(5):
        char = num % 37
        num //= 37
        message.append(newMap[char])
    # message.reverse()
    return str(message)


def decryptMessage(encryptedMessage, PrivateKey):
    '''
        utility function to decrypt the message
    '''
    print("encrypted message: ", encryptedMessage, end='\n', flush=True)
    decryptedBlock = pow(
        int(encryptedMessage), PrivateKey[0], PrivateKey[1])
    return decryptedBlock


def initiateData():
    ''' 
        utility function to create the mapping between the characters and the numbers
    '''
    conversionMap = {str(i): i for i in range(10)}
    conversionMap2 = {chr(char): i for i, char in zip(
        range(10, 37), range(ord('a'), ord('z')+1))}
    conversionMap.update(conversionMap2)
    conversionMap[' '] = 36
    return conversionMap


def evaluateE(phi):
    '''
        utility function to evaluate the value of e
    '''
    e = 2
    while True:
        if gcd(e, phi) == 1:
            break
        e += 1
    return e


def evaluateD(e, phi):
    '''
        utility function to evaluate the value of d
    '''
    return pow(e, -1, phi)


def nBitRandom(n):
    '''
        utility function to generate a number with certain number of bits
    '''
    return(random.randrange(2**(n-1)+1, 2**n-1))


# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)

        # Test divisibility by pre-generated
        # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            return pc


def isMillerRabinPassed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def generateRandomPrime(numberOfBits):
    '''
        utility function used to generate random prime numbers
    '''
    while True:
        n = numberOfBits
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            return prime_candidate


def applyingRSA(sizeInBytes=1024):
    '''
        C = M^e (mod n)
        M = C^d mod n = ((M)^e^d) mod n = M^(ed) mod n
        Both sender and receiver must know the value of n. The sender knows the
        value of e, and only the receiver knows the value of d.
        Here we will just generate the data. 
        our public key and our private key. 
    '''

    # 1. choosing two prime numbers
    p = generateRandomPrime(sizeInBytes)
    q = generateRandomPrime(sizeInBytes)

    print(p, q)

    # 2. calculating n
    n = p*q  # 7,908,826,517
    # 3. calculating phi(n)
    phi = (p-1)*(q-1)  # 7,907,818,380
    # 4. choosing e, it should be coprime with phi(n)
    # gcd (41, 7,907,818,380) = 1, I have calculated it manually.
    e = evaluateE(phi)
    # 5. calculating d
    # ! this is the inverse of the e mod phi(n) -> this should kept secret and only the receiver should know it.
    d = evaluateD(e, phi)
    publicKey = (e, n)
    privateKey = (d, n)

    print(
        f'public key is {publicKey},while the privet one is {privateKey}', flush=True)
    return publicKey, privateKey


def send(msg, client):
    '''
        utility function to send the message from the client to the server
    '''
    MSG = msg.encode(FORMAT)
    # the length of the message
    MSG_LEN = len(MSG)
    # send the length of the message
    send_len = str(MSG_LEN).encode(FORMAT)
    # add the header to the length of the message
    # el satr da m3nah eny b7oot el header el awl fl message, w b3den
    # ba7ot el message baa
    send_len += b' ' * (HEADER - len(send_len))
    # send the length of the message
    client.send(send_len)
    # send the message
    client.send(MSG)

 # generating keys for second user.
while True:
    number_of_bits = input(
        'Please Enter the number of bits you want to use in key generation: ')
    number_of_bits = int(number_of_bits)
    if number_of_bits > 20:
        break
    else:
        print('Please enter a number greater than 20')
PublicKey, PrivateKey = applyingRSA(sizeInBytes=int(number_of_bits))


def client(conn, addr, clients):
    '''
        this function is used to handle the client
        arguments:
        conn: the socket used to connect to the client
        addr: the address of the client
        clients: the list of other clients to be able to send them messages of others. clients
    '''
    print(f'initiating new client with IP address = {addr}')
    # this variable indicate whethere the client is connected or not?
    connected = True
    send(str(PublicKey[0]), conn)
    send(str(PublicKey[1]), conn)

    # 1. define the data
    conversionMap = initiateData()

    while connected:
        '''
            lazm n3rf toul el resala elly el user ba3tha, bs fe 7alet 
            el assignment bta3na, fa ehna already 3arfen eno byb3t 5 chars
            per message. 
        '''
        # This line means that whenever the server recieves any message
        # it should reserve a place in the memory with size = HEADER in bits
        # then decode it using the used Format.
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if(msg_len):
            # msg is string, so we want to convert it into int
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONECTIONCONDITION:
                connected = False
                continue
            # 7. decrypt the message using the private key on recieving side
            decryptedMessages = decryptMessage(
                encryptedMessage=msg, PrivateKey=PrivateKey)
            print('decryptedMessages: ', decryptedMessages, flush=True)
            # 8. get the original plain text
            originalMessage = getPlainTextAfterDecryption(
                decryptedMessages, conversionMap)
            # 9. print the message
            print('originalMessage: ', originalMessage, flush=True)
