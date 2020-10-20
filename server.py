import socket
import threading
import const

# create a socket instance type AF_INET, with stream data type (TCP protocol)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to defined addres
server.bind(const.ADDR)


def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(const.HEADER).decode(const.FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(const.FORMAT)
            if msg == const.DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()


def start():
    """Start server and handle new connections using threading."""
    server.listen()
    print(f"[LISTENING]: server up and running on {const.ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTOINS]: {threading.activeCount() - 1}")


start()
