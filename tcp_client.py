#!/usr/bin/env python3

import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])  

while True: 
    for item in sys.stdin: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        byte = bytearray(item, 'utf-8')
        s.send(byte)
        data = s.recv(1024)
        print('Received', repr(data))