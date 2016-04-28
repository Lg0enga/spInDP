#!/usr/bin/python
import socket
import atexit
import subprocess

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.42.0.70"
port = 8000
print (host)
print (port)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))

serversocket.listen(5)
print ('server started and listening')
while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!")
    data = clientsocket.recv(1024).decode()
    print (data)
    r='REceieve'
    if data == 'walk1':
	   execfile("walk/walk1.py")       
    if data == 'walk2':
	   execfile("walk/walk2.py")
    if data == 'walk3':
        subprocess.call(['python walk/walk4.py'], shell=True).split()

    





