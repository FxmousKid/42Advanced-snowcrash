#!/usr/bin/env python3
# a simple tcp server

import socket,os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('', 6969))  
sock.listen(5)


while True:  
    connection,address = sock.accept()  
    buf = connection.recv(1024)  
    print(buf)
    connection.send(buf)    		
    connection.close()