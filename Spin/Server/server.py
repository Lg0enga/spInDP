#!/usr/bin/python
import socket
import atexit
import subprocess
import sys
import cPickle
from threading import Thread
from multiprocessing import Process, Queue

sys.path.insert(0, '/home/pi/spInDP/Spin/Loopscripts')

from walk_test import Walk
walk = Walk()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.42.0.76', 8000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
serversocket.bind(server_address)
serversocket.listen(1)

i = 1
q = Queue()
q.put([0,0])
p = Process(target=walk.walk, args=(q, ))
p.start()

#p = Process(target = walk.walk(0, 1023))
#p.start()

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = serversocket.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        while True:
            data = connection.recv(1024)
            if data:

                data_arr = cPickle.loads(data)

                x = int(data_arr[0])
                y = int(data_arr[1])

                if  y > -1023 and y < 1023:
                    print "Y-waarde:", y
                    q.put(data_arr)
                else:
                    print "X-waarde:", x
                    if x > -1023 and x < 1023:
                        q.put(data_arr)
                    else:
                        walk.stop()

    finally:
        # Clean up the connection
        connection.close()
        #p.join()

    #r='REceieve'
    #if data == 'walk1':
	   #execfile("walk/walk1.py")
    #   subprocess.Popen([sys.executable, 'walk/walk1.py', '--username', 'pi'])
    #if data == 'walk2':
	  # execfile("/home/pi/spInDP/Spin/Loopscripts/test2.py",  globals ())
    #if data == 'walk3':
     #   subprocess.call(['/home/pi/spInDP/Spin/Loopscripts/len.py'], shell=True).split()
