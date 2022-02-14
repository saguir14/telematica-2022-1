
import socket
import os
import sys
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)


def main(host):
    HOST, PORT = host, 80
    request = f"GET / HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n".encode()
    response = ""
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.connect((HOST, PORT))
        print("Connecting...")
        sock.sendall(request)
        print("Sending data...")
        while True:
            recv = sock.recv(1024)
            if recv == b'':
                break
            response += recv.decode()
        print("The response has been received correctly...")

    with open('localfile.txt', 'w') as f:
        f.write(response)

    with open("localfile.txt", 'r') as fp:
        lines = fp.readlines()
        if "Content-Type: application/pdf" == lines[9].partition(';')[0] :
            ext = '.pdf'
        if "Content-Type: text/html" == lines[9].partition(';')[0] :
            ext = '.html'

    with open("localfile"+ext, 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [0,1,2,3,4,5,6,7,8,9]:
                fp.write(line)

    if os.path.exists("localfile.txt"):
        os.remove("localfile.txt")

    print("Your local file is done")

if __name__ == "__main__":
    main(sys.argv[1])
