'''
Module ex17

An example script to make a HTTP request using socket api
'''

import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('www.ntu.edu.sg', 80)
    # addr = ('165.225.96.34', 9480) # through proxy address
    client.connect(addr)

    req = 'GET /home/ehchua/programming/ HTTP/1.1'
    req += '\nHost: www.ntu.edu.sg'
    req += '\nAccept: text/html'
    req += '\nConnection: close\n\n'

    client.send(req.encode())
    output = ''
    while True:
        resp = client.recv(1024)
        if not resp: break
        output += resp.decode()

    print(output)

if __name__=='__main__': main()