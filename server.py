import socket, threading, argparse, const, utils

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
server_addr = (const.DEFAULT_SERVER, args.port)
server.bind(server_addr)


def handleClient(conn: socket.socket, addr: tuple):
    """Handle connected client."""
    print(f"[NEW CONNECTION]: {addr}")
    # do stuff
    utils.receiveFile(conn)
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