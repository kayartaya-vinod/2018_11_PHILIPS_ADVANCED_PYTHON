'''
Module ex18_server

Waits for a client to connect, gets a message, and sends it back
in upper case version of the same
'''

import socket

def main():
    server = socket.socket()
    addr = ('', 9999)
    server.bind(addr)
    server.listen(5)
    print('Server started...')

    while True:
        print('Waiting for connections...')
        (client, client_addr) = server.accept()
        print('Got a connection!')
        text = client.recv(1024)
        text = text.decode()
        print('[SERVER] recd from %s: %s' % (client_addr, text))
        client.send(text.upper().encode())
        client.close()

        if text=='QUIT': break

    server.close()

if __name__=='__main__': main()