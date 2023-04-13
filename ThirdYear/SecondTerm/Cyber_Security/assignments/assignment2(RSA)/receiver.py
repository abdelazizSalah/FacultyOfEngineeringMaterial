# from utilityFunctions import encryptMessages, generateBlockToBeSent, cleanData, initiateData, applyingRSA, decryptMessage, getPlainTextAfterDecryption
import socket
import numpy as np
import threading
from reciverUtilities import client

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
