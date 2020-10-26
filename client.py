import socket, argparse, utils, const

def sendRequest(sock: socket.socket, request_header: dict) -> int:
    """Send request to a connected socket."""
    # send request header, pass possible error 
    if utils.sendMessage(sock, str(request_header)) == 1:
        return 1

    # make request
    if request_header["method"] == "list":
        utils.printList(eval(utils.recvMessage(sock, message_len=const.HUGE_MESSAGE)))
    # check if filename argument is given
    elif not request_header["filename"]:
        print("ERROR: filename argument required for get/post")
    elif request_header["method"] == "post":
            utils.sendFile(sock, request_header["filename"])
    elif request_header["method"] == "get":
        utils.recvFile(sock, request_header["filename"])
    # shouldn't get here
    else:
        print("ERROR: unknown metehod.") 


if __name__ == "__main__":
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
        'filename', 
        metavar="filename", 
        help='File to get/post on server. [text.txt]', 
        nargs='?')
    args = parser.parse_args()

    # server config
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if args.hostname == "localhost":
        args.hostnmae = "0.0.0.0"
    addr = (args.hostname, args.port)
    
    # spin up the server
    try: 
        client.connect(addr)
        # send request
        request_header = {
            "method": args.method,
            "filename": args.filename
        }
        sendRequest(client, request_header)
    except ConnectionRefusedError:
        print("ERROR: invalid hostname or port.")


