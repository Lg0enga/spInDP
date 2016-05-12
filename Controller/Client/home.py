#!/usr/bin/env python
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
from dans import DansWindow
from loop import LoopWindow
from roll import RollWindow
from balloon import BalloonWindow
from video import VideoWindow

import socket


qtCreatorFile = "home.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class HomeWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showFullScreen()
        self.progressBar.setValue(85)
        self.DansButton.clicked.connect(self.DansClick)
        self.LoopButton.clicked.connect(self.LoopClick)
        self.RollButton.clicked.connect(self.RollClick)
        self.BalloonButton.clicked.connect(self.BalloonClick)
        self.VideoButton.clicked.connect(self.VideoClick)
        self.ExitButton.clicked.connect(QtCore.QCoreApplication.quit)

    def RollClick(self):
	self.FG = RollWindow()
	self.FG.show()
        self.progressBar.setValue(20)
        self.progressBar.setStyleSheet("QProgressBar{border: 2px solid grey;text-align: center}QProgressBar::chunk {background-color: red;width: 5px;margin: 1px;}")

    def DansClick(self):
	self.FD = DansWindow()
	self.FD.show()
        self.progressBar.setValue(95)
        self.progressBar.setStyleSheet("")

    def LoopClick(self):
	self.FL = LoopWindow()
	self.FL.show()

    def BalloonClick(self):
        self.GD = BalloonWindow()
        self.GD.show()

    def VideoClick(self):
        self.GW = VideoWindow()
        self.GW.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())
