'''
Module ex18_client

A simple socket client to talk to a socket server
'''

import socket
import sys

def main():
    addr = (socket.gethostname(), 9999)
    client = socket.socket()
    client.connect(addr)

    text = sys.argv[1]
    client.send(text.encode())
    text = client.recv(1024)
    client.close()
    print('Server responded: ' + text.decode())

if __name__=='__main__': main()

