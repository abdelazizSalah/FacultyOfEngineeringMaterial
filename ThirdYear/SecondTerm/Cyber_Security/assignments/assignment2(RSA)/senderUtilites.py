import socket
import numpy as np
import rsa
# ? initiating the connections

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
    '''
        utility function to read the message from the server to the client
    '''
    PrivateKey = (d, n)
    print(f'PrivateKey = {PrivateKey}', flush=True)
    msg_len = client.recv(HEADER).decode(FORMAT)
    if(msg_len):
        # msg is string, so we want to convert it into int
        msg_len = int(msg_len)
        msg = client.recv(msg_len).decode(FORMAT)
        # 7. decrypt the message using the private key on recieving side
        decryptedMessages = decryptMessage(
            encryptedMessage=msg, PrivateKey=PrivateKey)
        print('decryptedMessages: ', decryptedMessages, flush=True)
        # 8. get the original plain text
        originalMessage = getPlainTextAfterDecryption(
            decryptedMessages, conversionMap)
        # 9. print the message
        print('originalMessage: ', str(originalMessage), flush=True)


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
    # message.reverse()
    return message


def generateBlockToBeSent(message, conversionMap):
    '''
        utility function to generate the blocks to be sent each with len = 5
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


def encryptMessages(sendingBlocks, PublicKey):
    '''
        utility function to encrypt the message
    '''
    encryptedMessages = []
    for block in sendingBlocks:
        print('------>', block, PublicKey[0], PublicKey[1])
        encryptedBlock = pow(int(block), PublicKey[0], PublicKey[1])
        encryptedMessages.append(encryptedBlock)
    return encryptedMessages


def getPlainTextAfterDecryption(num, conversionMap):
    '''
        this is a utility function used to return the decrypted message from the number
        into the original plain text
    '''
    message = []
    # this to reverse the mapping. so we can get the character from the number
    newMap = {v: k for k, v in conversionMap.items()}
    for i in range(5):
        char = np.mod(int(np.floor(np.divide(num, np.power(37, i)))), 37)
        num -= char
        print(char)
        message.append(newMap[char])
    # message.reverse()
    return str(message)


def decryptMessage(encryptedMessage, PrivateKey):
    '''
        utility function to decrypt the message
    '''
    print("encrypted message: ", encryptedMessage, end='\n', flush=True)
    print(f"d = {PrivateKey[0]} , n= {PrivateKey[1]} ", flush=True)
    decryptedBlock = pow(
        int(encryptedMessage[0]), PrivateKey[0], PrivateKey[1])
    return decryptedBlock
