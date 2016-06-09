import thread
import threading
import time
import socket
from threading import Thread
from buffer import Buffer
from client import Client

class Server(Thread):

    def __init__(self, Buffer):
        self._Clients = []
        self._Buffer = Buffer
        self._Exit = False
        self._Identify = 10

    def Start(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind(('172.24.1.1', 8000))
        serverSocket.listen(1)

        print "Connected"

        while not self._Exit:
            clientSocket, address = serverSocket.accept()
            client = Client(clientSocket, self._Identify)
            self._Clients.append(client)
            self._Identify += 1

            print("Connected with " + address[0] + ":" + str(address[1]) + "\n")

            try:
                t = threading.Thread(target=self.Listen, args = (client,))
                t.deamon = True
                t.start()
            except:
                print("Error: Unable to start thread \n")

            time.sleep(1)

    def Listen(self, clientSocket):
        while not self._Exit:
            try:
                data = clientSocket.getClientSocket().recv(1024)
                self._Buffer.Stack(data)
                time.sleep(0.001)
            except:
                print("Client " + clientSocket.getClientID() + " has disconnected.")
                break

    def Send(self, data, iD):
        iD = iD[3:5]

        clientSocket = 0
        if len(str(data)) > 0:
            for client in self._Clients:
                if client.getClientID() == iD:
                    clientSocket = client
                    break
            try:
                clientSocket.getClientSocket().send(str(data))
            except:
                pass

    def Exit(self):
        self._Exit = True
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.connect(('172.24.1.1', 8000))
