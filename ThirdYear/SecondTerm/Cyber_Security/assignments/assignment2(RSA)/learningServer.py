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
        # el loop de el hadaf menha enny lama wa7ed yeb3tly 7aga, aro7 ab3t el 7aga de
        # le kol el nas el tanya m3ada howa.
        # aknha fe game kda fahem.
        #! msh muhema awy lel assignment bt3na.
        for client in clients:
            if client != conn:
                send(msg, client)
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


start()
