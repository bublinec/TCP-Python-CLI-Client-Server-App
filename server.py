import socket, threading, argparse

DATA_SIZE = 1024
SERVER = "0.0.0.0"

# use parser
parser = argparse.ArgumentParser(description='Perform a server request.')
parser.add_argument(
    'port', 
    metavar="port", 
    help='Port number used for connection. [8000]', 
    type=int)
args = parser.parse_args()

# server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = (SERVER, args.port)
server.bind(server_addr)


def handleClient(conn: socket.socket, addr: tuple):
    """Handle file receving from client."""
    print(f"[NEW CONNECTION]: {addr}")
    # receive file
    with open('received_file.txt', 'wb') as f:
        data = conn.recv(DATA_SIZE)
        while data:
            print(f"[RECEVING]: {DATA_SIZE} bytes from {addr}")
            f.write(data)
            data = conn.recv(DATA_SIZE)
    print(f"[FINISHED]: closing connection with {addr}")
    conn.close()

def startServer():
    """Start server and handle new connections using threads."""
    server.listen()
    print(f"[LISTENING]: server running on {server_addr}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()

startServer()