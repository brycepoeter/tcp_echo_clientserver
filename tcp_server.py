#!/usr/bin/env python3

import socket
import sys

port = int(sys.argv[1])
print('Listening on port ', port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(5)
while True:
    client, addr = s.accept()
    data = client.recv(1024)
    print('Sent/received', repr(data))
    client.send(data) 
    client.close()

            