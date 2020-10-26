import socket, threading, argparse, os, const, utils


def handleRequest(conn: socket.socket) -> int:
    # receive request method
    try: 
        request_header = eval(utils.recvMessage(conn))
    except SyntaxError:
        print("ERROR while receiving header")
        return 1

    # handle request
    if request_header["method"] == "list":
        utils.sendMessage(conn, os.listdir(), message_len=const.HUGE_MESSAGE)
    elif request_header["method"] == "post":
        utils.recvFile(conn, request_header["filename"])
    elif request_header["method"] == "get":
        utils.sendFile(conn, request_header["filename"])
    # shouldn't get here
    else:
        print("ERROR: unknown metehod.") 
        

def handleClient(conn: socket.socket, addr: tuple):
    """Handle connected client."""
    print(f"[NEW CONNECTION]: {addr}")
    handleRequest(conn)
    conn.close()


def startServer():
    """Start server and handle new connections using threads."""
    server.listen()
    print(f"[LISTENING]: server running on {server_addr}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    # exception to get a nice message instead of an error when shutting down server
    try:
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

        startServer()
        
    except KeyboardInterrupt:
        print()
        print('[SHUTING DOWN SERVER]: Goodbye!')
