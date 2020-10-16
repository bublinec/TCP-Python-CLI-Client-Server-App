import socket
import threading

HEADER = 64
FORMAT = "utf-8"
PORT = 5050
# get my local IP
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
# create a socket instance type AF_INET, with stream data type (TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to defined addres
server.bind(ADDR)


def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")
    conn.close()


def start():
    """Start server and handle new connections using threading."""
    server.listen()
    print(f"[LISTENING]: server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTOINS]: {threading.activeCount() - 1}")


print("[STARTING]: starting the server")
start()
