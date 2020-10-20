import socket
import const
import argparse

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = ""
ADDR = (SERVER, PORT)

# parser setup
parser = argparse.ArgumentParser(description='Client script arguments:')
parser.add_argument('method', metavar="method", type=str, help='Specify request method.')

# socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(const.ADDR)


def send(msg):
    # encode message into correct format
    message = msg.encode(const.FORMAT)
    # send message length
    msg_len = len(message)
    send_length = str(msg_len).encode(const.FORMAT)
    send_length += b' ' * (const.HEADER - len(send_length))
    client.send(send_length)
    # send message itself
    client.send(message)


# parse arguments
args = parser.parse_args()
print((args.method))

send("Hello World!")