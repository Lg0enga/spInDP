#!/usr/bin/env python
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
#from home import HomeWindow


qtCreatorFile = "dans.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class DansWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(0, 30, 491, 298)
        self.BackButton.clicked.connect(self.BackClick)
        #self.Tang0Button.clicked.connect(QtCore.QCoreApplication.quit)

    def BackClick(self):
        self.close()
    
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DansWindow()
    window.show()
    sys.exit(app.exec_())
