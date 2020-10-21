import socket, argparse, utils

DATA_SIZE = 1024

# use parser
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
    nargs='*') # TO DO: HANDLE THIS
args = parser.parse_args()

# setup connection to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (args.hostname, args.port)
client.connect(addr)


utils.sendFile("test.txt", client)