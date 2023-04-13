import socket
import numpy as np
import rsa
# ? initiating the connections

# the port on which we are connected
PORT = 5050
# the used format.
FORMAT = 'utf-8'
# condition of closing
DISCONECTIONCONDITION = 'DES'
# Header
HEADER = 64

# here, the server must be fixed
SERVER = '127.0.0.1'

# define ADDR
ADDR = (SERVER, PORT)

# define client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # make the connection on certain address
# client.connect(ADDR)


def send(msg):
    '''
        utility function to send the message from the client to the server
    '''
    msg = str(msg)
    print('msg: ', msg, flush=True)
    MSG = msg.encode(FORMAT)
    # the length of the message
    MSG_LEN = len(MSG)
    # MSG_LEN = 5
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


def read(d, n, conversionMap):
    PrivateKey = (d, n)
    '''
        utility function to read the message from the server to the client
    '''
    msg_len = client.recv(HEADER).decode(FORMAT)
    if(msg_len):
        # msg is string, so we want to convert it into int
        msg_len = int(msg_len)
        msg = client.recv(msg_len).decode(FORMAT)
        # 7. decrypt the message using the private key on recieving side
        decryptedMessages = decryptMessage(
            encryptedMessage=msg, PrivateKey=PrivateKey)
        # 8. get the original plain text
        originalMessage = getPlainTextAfterDecryption(
            decryptedMessages, conversionMap)
        # 9. print the message
        print('originalMessage: ', originalMessage, flush=True)


def initiateData():
    ''' 
        utility function to initiate the data
    '''
    conversionMap = {str(i): i for i in range(10)}
    conversionMap2 = {chr(char): i for i, char in zip(
        range(10, 37), range(ord('a'), ord('z')+1))}
    conversionMap.update(conversionMap2)
    conversionMap[' '] = 36
    return conversionMap


def checkChar(char, conversionMap):
    '''
        utility function to check whethere the character is in our map or not  
    '''
    if char in conversionMap:
        return True
    return False


def evaluateNumber(char, conversionMap, i):
    '''
        utility function to evaluate the number of each character using our scheme    
    '''
    return np.multiply(conversionMap[char], np.power(37, i))


def cleanData(message, conversionMap):
    '''
        utility function to remove the extra characters and fill the missing ones with spaces
    '''
    message = message.lower()
    message = list(message)
    for i in range(len(message)):
        if checkChar(message[i], conversionMap) != True:
            message[i] = ' '
    # fill the missing characters as spaces to create equally sized blocks
    remainder = len(message) % 5
    if remainder != 0:
        while remainder != 5:
            message.append(' ')
            remainder += 1
    # reversing the message to follow our scheme :)
    message.reverse()
    return message


def generateBlockToBeSent(message, conversionMap):
    '''
        utility function to generate the blocks to be sent
    '''
    sendingBlocks = []
    counter = 0
    newBlock = 0
    for i in range(len(message)):
        if(counter == 5):
            sendingBlocks.append(newBlock)
            newBlock = 0
            counter = 0
        # this part should be done regardless the value of counter
        newBlock += evaluateNumber(message[i], conversionMap, counter)
        counter += 1
    # this check because if len % 5 == 0 then the last appending will not be done.
    if(counter == 5):
        sendingBlocks.append(newBlock)
    return sendingBlocks


def applyingRSA(dynamic=False, sizeInBytes=1024):
    '''
        C = M^e (mod n)
        M = C^d mod n = ((M)^e^d) mod n = M^(ed) mod n
        Both sender and receiver must know the value of n. The sender knows the
        value of e, and only the receiver knows the value of d.
        Here we will just generate the data. 
        our public key and our private key. 
    '''
    # 1. choosing two prime numbers
    # TODO: to be generated
    p = 7919
    q = 5839
    # 2. calculating n
    n = p*q
    # 3. calculating phi(n)
    phi = (p-1)*(q-1)
    # 4. choosing e, it should be coprime with phi(n)
    # TODO: to be generated
    e = 41  # gcd (41, 46239041) = 1, I have calculated it manually.
    # 5. calculating d
    # ! this is the inverse of the e mod phi(n) -> this should kept secret and only the receiver should know it.
    d = 23676365

    if dynamic == False:
        publicKey = (e, n)
        privateKey = (d, n)
    else:
        publicKey, privateKey = rsa.newkeys(sizeInBytes)
    return (e, n), (d, n)


def fastModularExponentiationusingPowOf2(b, e, n):
    '''
         consider the exponent is a 2 pow (k)
         so now we can reduce the number of computations by using powers of 2
         so for example if we want to compute 7 pow (128) so we can compute it in such way
         7 pow (128) = 7 pow (64) * 7 pow (64)
         7 pow (64) = 7 pow (32) * 7 pow (32)
         7 pow (32) = 7 pow (16) * 7 pow (16)
         7 pow (16) = 7 pow (8) * 7 pow (8)
         7 pow (8) = 7 pow (4) * 7 pow (4)
         7 pow (4) = 7 pow (2) * 7 pow (2)
         7 pow (2) = 7 pow (1) * 7 pow (1)
         so we can compute it in O(log(e)) instead of O(e)
         and if e was not multiple of 2 pow (k) then you can represent e in the binary formate and use it as follows:
         let e = 13
              |8 |4| 2| 1|
         ------------------
         13 = |1 |1| 0| 1|
         so we can compute it as follows:
         7 pow (13) = 7 pow (8) * 7 pow (4) * 7 pow (1) -> so 7 pow (8) and 7 pow(4) can be computed with pow of 2 and at the end
         we can multiply the result by 7 pow (1) which is 7.
         so we can compute it in O(2log(e)) atmost.
         so we can implement it as follows:
    '''
    c = 1
    while(e > 0):
        if(e & 1):  # if the exponent is odd
            c = np.mod(np.multiply(c, b), n)  # multiply the result by the base
        b = np.mod(b, n)
        b = np.mod(np.square(b), n)  # square the base
        e //= 2
    return c


def encryptMessages(sendingBlocks, PublicKey):
    '''
        utility function to encrypt the message
    '''
    encryptedMessages = []
    for block in sendingBlocks:
        # this loop to avoid overflow
        encryptedBlock = fastModularExponentiationusingPowOf2(
            int(block), PublicKey[0], PublicKey[1])  # C = M^e (mod n)
        encryptedMessages.append(encryptedBlock)
    return encryptedMessages


def getPlainTextAfterDecryption(num, conversionMap):
    '''
        this is a utility function used to return the decrypted message from the number
        into the original plain text
    '''
    message = []
    newMap = {v: k for k, v in conversionMap.items()}
    for i in range(5):
        char = np.mod(int(np.floor(np.divide(num, np.power(37, i)))), 37)
        message.append(newMap[char])
    message.reverse()
    return str(message)


def decryptMessage(encryptedMessage, PrivateKey):
    '''
        utility function to decrypt the message
    '''
    print("encrypted message: ", encryptedMessage, end='\n', flush=True)
    # decryptedMessages = []
    # for block in encryptedMessage:
    # print("block: ", encryptedMessage, end='\n')
    # this loop to avoid overflow
    decryptedBlock = fastModularExponentiationusingPowOf2(
        int(encryptedMessage), PrivateKey[0], PrivateKey[1])  # M = C^d mod n
    # decryptedMessages.append(decryptedBlock)
    return decryptedBlock
