import os, socket, const


def printList(l: list):
    print("\n Server files: \n")
    for item in l:
        print(item)


def sendMessage(sock: socket.socket, message: str, message_len=const.SHORT_MESSAGE) -> int:
    """Send a short message to connected socket."""
    # check message len
    if len(message) > message_len:
        print(f"ERROR: filename too long")
        return 1
    # padd message so it matches the len
    padded_message = f"{message}{(message_len - len(message)) * ' '}"
    sock.send(padded_message.encode(const.ENCODING))
    print(f"[SHORT MESSAGE SENT] to {sock.getpeername()}: {message}")


def recvMessage(sock: socket.socket, message_len=const.SHORT_MESSAGE) -> str:
    """Return short message received from connected socket."""
    message = sock.recv(message_len).strip().decode(const.ENCODING)
    print(f"[SHORT MESSAGE RECEIVED] from {sock.getsockname()}: {message}")
    return message


def sendFile(sock: socket.socket, filename: str):
    """Send a file to connected socket."""
    print(f"[SENDING FILE] to {sock.getpeername()}")
    with open(filename, 'rb') as f:
        while True:
            data = f.read(const.LONG_MESSAGE)
            sock.send(data)
            print(f"[SEND] {len(data)} bytes")
            if len(data) < const.LONG_MESSAGE:
                break
    print("[FINISHED]: file sent")


def recvFile(sock: socket.socket, filename: str, overwrite=False):
    """Receive a file from connected socket."""
    print(f"[RECEIVING FILE] from {sock.getsockname()}")
    # avoid overwriting files with the same name
    if not overwrite:
        files = os.listdir()
        while filename in files:
            filename = "received-" + filename
    # receive file
    with open(filename, 'wb') as f:
        while True:
            data = sock.recv(const.LONG_MESSAGE)
            print(f"[RECEIVED] {len(data)} bytes")
            f.write(data)
            if len(data) < const.LONG_MESSAGE:
                break
    print(f"[FINISHED]: file received")