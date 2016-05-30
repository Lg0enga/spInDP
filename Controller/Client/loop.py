#!/usr/bin/env python
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
import socket


qtCreatorFile = "loop.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LoopWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(0, 30, 491, 298)
        self.BackButton.clicked.connect(self.BackClick)
        self.Loop1Button.clicked.connect(self.Loop1Click)
        self.Loop2Button.clicked.connect(self.Loop2Click)
        self.Loop3Button.clicked.connect(self.Loop3Click)
        self.WalkyButton.clicked.connect(QtCore.QCoreApplication.quit)

    def BackClick(self):
        self.close()

    def Loop1Click(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('10.42.0.76', 8000))
        clientsocket.send('walk1')
        clientsocket.shutdown()

    def Loop2Click(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('10.42.0.76', 8000))
        clientsocket.send('walk2')
        clientsocket.listen(5)
        print clientsocket.recv(1024)
        clientsocket.shutdown()

    def Loop3Click(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('10.42.0.76', 8000))
        clientsocket.send('walk3')
        clientsocket.shutdown()

    
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = LoopWindow()
    window.show()
    sys.exit(app.exec_())
