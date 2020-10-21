import const, socket

def sendFile(filename: str, socket: socket.socket, data_size=const.DATA_SIZE):
    """Send a file using socket."""
    print(f"[SENDING FILE] to {socket.getpeername()}")
    socket.send(filename.encode(const.ENCODING))
    with open(filename,'rb') as f:
        data = f.read(data_size)
        while (data):
            socket.send(data)
            print(f"[SENDING] {data_size} bytes")
            data = f.read(data_size)
    print("[FINISHED]: file sent")


def receiveFile(conn: socket.socket):
    """Receive a file from connection."""
    print(f"[RECEIVING FILE] from {conn.getsockname()}")
    filename = conn.recv(const.MAX_FILENAME_SIZE)
    with open(filename, 'wb') as f:
        data = conn.recv(const.DATA_SIZE)
        while data:
            print(f"[RECEVING] {const.DATA_SIZE} bytes")
            f.write(data)
            data = conn.recv(const.DATA_SIZE)
    print(f"[FINISHED]: file received")