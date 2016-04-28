#!/usr/bin/env python
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
from dans import DansWindow
from loop import LoopWindow
import socket


qtCreatorFile = "home.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class HomeWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showFullScreen()
        self.DansButton.clicked.connect(self.DansClick)
        self.LoopButton.clicked.connect(self.LoopClick)
        self.ExitButton.clicked.connect(QtCore.QCoreApplication.quit)

    def DansClick(self):
        self.FD = DansWindow()
        self.FD.show()

    def LoopClick(self):
        self.FL = LoopWindow()
        self.FL.show()    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())
