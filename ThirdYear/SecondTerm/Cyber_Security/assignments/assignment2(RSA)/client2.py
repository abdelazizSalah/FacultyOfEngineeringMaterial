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
import threading
import time
import socket

from utilityFunctions import *
#!----------------------------- building the program ------------------------------------------!#


# recieve the public key of the server

msg_len = client.recv(HEADER).decode(FORMAT)
e = client.recv(int(msg_len)).decode(FORMAT)
e = int(e)
msg_len = client.recv(HEADER).decode(FORMAT)
n = client.recv(int(msg_len)).decode(FORMAT)
n = int(n)
PublicKey = (e, n)

print(PublicKey)

while (1):

    # 1. define the data
    conversionMap = initiateData()

    # 2. get the message from the user
    message = input("Enter the message: ")
    if(message == DISCONECTIONCONDITION):
        break
    # send(message)
    # 3. clean the message
    message = cleanData(message=message, conversionMap=conversionMap)

    # 4. converting the message into numbers each 5 chars together
    sendingBlocks = generateBlockToBeSent(
        message=message, conversionMap=conversionMap)

    print('sendingBlocks: ', sendingBlocks, flush=True)
    # 5. encrypt the message using the public key
    encryptedMessages = encryptMessages(
        sendingBlocks=sendingBlocks, PublicKey=PublicKey)

    # 6. send the message to the receiver
    # TODO?: send the message to the receiver and make the communication
    # ! hena ehna 3auzen enna nb3t lel server baa kol el messages.
    for message in encryptedMessages:
        send(message)
        # time.sleep(1)

    # # then wait till the receiver sends the message back
    # read(PrivateKey[0], PrivateKey[1], conversionMap)

# closing the connection
send(DISCONECTIONCONDITION)
