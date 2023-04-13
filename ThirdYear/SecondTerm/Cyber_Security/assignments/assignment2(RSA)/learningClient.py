import socket
import threading
import time
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

# make the connection on certain address
client.connect(ADDR)


def send(msg):
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


def read():
    '''
        utility function to read the message from the server to the client
    '''
    msg_len = client.recv(HEADER).decode(FORMAT)
    if(msg_len):
        # msg is string, so we want to convert it into int
        print('msg_len: ', msg_len)
        msg_len = int(msg_len)
        msg = client.recv(msg_len).decode(FORMAT)
        print(msg)


x = ''
while (x != DISCONECTIONCONDITION):
    # threading
    thread = threading.Thread(target=read)
    thread.start()
    x = input('Enter the message to be sent: ')
    send(x)

# closing the connection
send(DISCONECTIONCONDITION)
