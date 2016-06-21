#!/usr/bin/python
import socket
import atexit
import subprocess
import sys
import cPickle


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('172.24.1.1', 8000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
serversocket.bind(server_address)
serversocket.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = serversocket.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        while True:
            data = connection.recv(1024)
            if data:
                print data
                data = data.replace("led", "")
                data_arr = cPickle.loads(data)
                r = int(data_arr[0])
                g = int(data_arr[1])
                b = int(data_arr[2])
                print r
                print g
                print b

    finally:
        # Clean up the connection
        connection.close()
