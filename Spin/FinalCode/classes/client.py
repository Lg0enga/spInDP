class Client(object):
    def __init__(self, clientSocket, clientID):

        self._ClientSocket = clientSocket
        self._ClientID = clientID

    def getClientID(self):
        return str(self._ClientID)

    def getClientSocket(self):
        return self._ClientSocket
