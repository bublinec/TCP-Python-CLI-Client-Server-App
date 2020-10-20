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
parser = argparse.ArgumentParser(description='Perform a server request.')
parser.add_argument(
    'hostname', 
    metavar="hostname",
    help='Server hostname (IPv4) to connect. [130.209.157.48]')
parser.add_argument(
    'port', 
    metavar="port", 
    help='Port number used for connection. [8000]', 
    type=int)
parser.add_argument(
    'method', 
    metavar="method", 
    help='Request method. [get/post/list]',
    choices=["get", "post", "list"]
    )
parser.add_argument(
    'files', 
    metavar="filename", 
    help='Filenames to get/post on server. [text1.txt test2.py]', 
    nargs='*')

# socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(const.ADDR)


def get_args() -> argparse.Namespace:
    args = parser.parse_args()
    # NOT SURE IF THIS IS THE RIGHT WAY TO HANDLE THIS
    if(args.method != "list" and args.files == []):
        raise ValueError("filename argument required for this method")
    return args


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


# get arguments
print(get_args())

send("Hello World!")