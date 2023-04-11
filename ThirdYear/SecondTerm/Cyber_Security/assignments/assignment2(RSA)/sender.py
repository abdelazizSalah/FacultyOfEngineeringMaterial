'''
    @Author Abdelaziz Salah Moahmmed 
    @Date 10/4/2023
    This is an RSA sender program. It takes a message and a public key
    and encrypts the message using the public key. The encrypted message
    is then sent to the receiver.
    @Algorithm is as follows:
    1. we define a map, which converts the 36 available characters to a number.
    as follows 
        [0 -> 0, 1 -> 1 ... 9 -> 9, a -> 10, b -> 11, ... z -> 35]
    2. if we find any different character, we deal with it simply as space.
    3. Read the message from the user.
    4. before implementing the RSA, we must code the input into numbers.
    5. our scheme is as follows: 
        - Convert any extra characters to spaces as specified above.
        - Group the plaintext into sets of five characters per group
        - If the last grouping does not have exactly five characters,then append some space to the end of the plaintext message to fill out the last grouping
        - Convert each group into a separate number as follows
            - group one is [c4,c3,c2,c1,c0]
            - then the number = c4*37^4 + c3*37^3 + c2*37^2 + c1*37^1 + c0*37^0
        - A decoding operation should be performed in the same way except that the process is reversed.
          A number is converted to its character grouping by using mod and div
'''

# ?  lets get our hands dirty :)
import numpy as np
import socket
import threading
# this library is used to send objects rather than strings
import pickle
import time

# the port on which we are connected
PORT = 5050
# the used format.
FORMAT = 'utf-8'
# condition of closing
DISCONECTIONCONDITION = 'DES'
# Header
HEADER = 64
# this is a dynamic way to get the IP address of the host.
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '127.0.0.1'
# local host IP '127.0.0.1'
ADDR = (SERVER, PORT)
# 3ndna haga esmha family w haga esmha type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


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
            print(
                f'the adress is:\t {addr} and the content of the message is:\n {msg}')
    # when we finish the connection we need to close it.
    print('closing the connection')
    conn.close()


def start():
    '''
        this function is used to start the server
    '''
    # keda enta m5ly el socket mstnya 7d yb3tlha 7aga.
    server.listen()
    print(f'The server is listening to {SERVER}')
    clients = []
    while True:
        '''
        Accept de btst2bl el data el gaylha mn ay client
        fa lama byb2a fe connection btrg3 7agten
        addr -> da el IP address bta3 el client
        conn -> da socket by3br 3n el connection el 7slt ben el client wl server
        '''
        conn, addr = server.accept()
        clients.append(conn)
        # now we want to apply parallelism
        '''
            Thread takes the function to be applied.    
            the argument to be sent to this function. 
        '''
        thread = threading.Thread(target=client, args=(conn, addr, clients))

        # lets start the thread
        thread.start()


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


def cleanData(message):
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


def applyingRSA():
    '''
        C = M^e (mod n)
        M = C^d mod n = ((M)^e^d) mod n = M^(ed) mod n
        Both sender and receiver must know the value of n. The sender knows the
        value of e, and only the receiver knows the value of d.
        Here we will just generate the data. 
        our public key and our private key. 
    '''
    # 1. choosing two prime numbers
    p = 7919
    q = 5839
    # 2. calculating n
    n = p*q
    # 3. calculating phi(n)
    phi = (p-1)*(q-1)
    # 4. choosing e, it should be coprime with phi(n)
    e = 41  # gcd (41, 46239041) = 1, I have calculated it manually.
    # 5. calculating d
    # ! this is the inverse of the e mod phi(n) -> this should kept secret and only the receiver should know it.
    d = 23676365
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
            block, PublicKey[0], PublicKey[1])  # C = M^e (mod n)
        encryptedMessages.append(encryptedBlock)
    return encryptedMessages


def decryptMessage(encryptedMessage, PrivateKey):
    '''
        utility function to decrypt the message
    '''
    decryptedMessages = []
    for block in encryptedMessage:
        # this loop to avoid overflow
        decryptedBlock = fastModularExponentiationusingPowOf2(
            block, PrivateKey[0], PrivateKey[1])  # M = C^d mod n
        decryptedMessages.append(decryptedBlock)
    return decryptedMessages


#!----------------------------- building the program ------------------------------------------!#
# 1. define the data
conversionMap = initiateData()

# 2. get the message from the user
message = input("Enter the message: ")

# 3. clean the message
message = cleanData(message)

# converting the message into numbers each 5 chars together
sendingBlocks = generateBlockToBeSent(
    message=message, conversionMap=conversionMap)

# 4. evaluate the public and private keys
PublicKey, PrivateKey = applyingRSA()

# 5. encrypt the message using the public key
encryptedMessages = encryptMessages(
    sendingBlocks=sendingBlocks, PublicKey=PublicKey)

# 6. send the message to the receiver
# TODO?: send the message to the receiver and make the communication

# 7. decrypt the message using the private key
decryptedMessages = decryptMessage(
    encryptedMessage=encryptedMessages, PrivateKey=PrivateKey)

# 8. print the message
print(decryptedMessages)
