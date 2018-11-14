import json
import socket

def main():
    p = {}
    p['name'] = 'Krish'
    p['city'] = 'Mysore'
    p['email'] = 'krish@example.com'
    p['phone'] = '9747464444'
    p['picture'] = None

    req = 'POST /api/contacts HTTP/1.1\n'
    req += 'Host: localhost:5000\n'
    req += 'Content-Type: application/json\n'
    req += 'Connection: close\n\n\n'
    req += json.dumps(p)

    print(req)
    

    client = socket.socket()
    client.connect(('localhost', 5000))
    client.send(req.encode())
    resp = client.recv(1024).decode()
    print(resp)

if __name__=='__main__': main()