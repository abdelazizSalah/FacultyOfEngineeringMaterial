# from utilityFunctions import encryptMessages, generateBlockToBeSent, cleanData, initiateData, applyingRSA, decryptMessage, getPlainTextAfterDecryption
import socket
import threading
import numpy as np
import rsa
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
    message.reverse()
    return str(message)


def decryptMessage(encryptedMessage, PrivateKey):
    '''
        utility function to decrypt the message
    '''
    print("encrypted message: ", encryptedMessage, end='\n', flush=True)
    print(f"d = {PrivateKey[0]} , n= {PrivateKey[1]} ", flush=True)
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
        if np.gcd(e, phi) == 1:
            break
        e += 1
    return e


def evaluateD(e, phi):
    '''
        utility function to evaluate the value of d
    '''
    # d = 2
    # while True:
    #     if (e*d) % phi == 1:
    #         break
    #     d += 1
    # return d
    return pow(e, -1, phi)


def applyingRSA(dynamic=False, sizeInBytes=1024, clientNum=1):
    '''
        C = M^e (mod n)
        M = C^d mod n = ((M)^e^d) mod n = M^(ed) mod n
        Both sender and receiver must know the value of n. The sender knows the
        value of e, and only the receiver knows the value of d.
        Here we will just generate the data. 
        our public key and our private key. 
    '''
    # 1. choosing two prime numbers
    if clientNum == 1:
        p = 1000231
        q = 7907
    else:
        p = 1196089
        q = 14071

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
    print(e, d, sep='------------------', flush=True)

    if dynamic == False:
        publicKey = (e, n)
        privateKey = (d, n)
    else:
        publicKey, privateKey = rsa.newkeys(sizeInBytes)
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
PublicKey, PrivateKey = applyingRSA(clientNum=2)


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
            print(f'length = {msg_len}', flush=True)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f'msgGatly kda {msg}', flush=True)

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
            print('originalMessage: ', str(originalMessage), flush=True)
        # el loop de el hadaf menha enny lama wa7ed yeb3tly 7aga, aro7 ab3t el 7aga de
        # le kol el nas el tanya m3ada howa.
        # aknha fe game kda fahem.
        #! msh muhema awy lel assignment bt3na.
        for client in clients:
            if client != conn:
                send(msg, client)


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
        print('threding the client')
        thread = threading.Thread(
            target=client, args=(conn, addr, clients))

        # lets start the thread
        thread.start()


start()
