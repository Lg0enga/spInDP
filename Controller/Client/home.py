#!/usr/bin/env python
#from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
from dans import DansWindow
from loop import LoopWindow
from roll import RollWindow
from balloon import BalloonWindow
from video import VideoWindow
import Adafruit_ADS1x15
import threading
import time
import os
import RPi.GPIO as GPIO   
from threading import Thread
import socket
import cPickle as pickle

#set GPIO settings
GPIO.setmode(GPIO.BCM)          
INPUT_PIN = 4           
GPIO.setup(INPUT_PIN, GPIO.IN)

#set GUI settings
qtCreatorFile = "home.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#set ADC Settings
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

#start socket for walking moves
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	clientsocket.connect(('10.42.0.76', 8000))
except :
	print "error socket"
#clientsocket.send("test")
# Theard for reading form ADC
class mythread(QtCore.QThread):
    def __init__(self,parent,n):
        QtCore.QThread.__init__(self,parent) 
        self.n=n

    def run(self):
        self.emit(QtCore.SIGNAL("total(PyQt_PyObject)"),self.n)
        i=0
        while (i<self.n):            
            self.emit(QtCore.SIGNAL("update()"))
            time.sleep(0.1)

# Main Thread window
class HomeWindow(QtGui.QMainWindow, Ui_MainWindow):    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showFullScreen()
	self.t=mythread(self,100)
        QtCore.QObject.connect(self.t, QtCore.SIGNAL("total(PyQt_PyObject)"), self.total)
        QtCore.QObject.connect(self.t, QtCore.SIGNAL("update()"), self.update)
        self.n=0
        self.t.start()
        self.DansButton.clicked.connect(self.DansClick)
        self.LoopButton.clicked.connect(self.LoopClick)
        self.RollButton.clicked.connect(self.RollClick)
        self.BalloonButton.clicked.connect(self.BalloonClick)
        self.VideoButton.clicked.connect(self.VideoClick)
        self.ExitButton.clicked.connect(self.ExitClick)
        self.xbar.setMaximum(1080)
        self.xbar.setMinimum(-1150)
        self.ybar.setMaximum(1080)
        self.ybar.setMinimum(-1090)

    def update(self):
        self.n+=1
        print self.n
        print int(-0.0821 * adc.read_adc(0, gain=GAIN) + 1045.2)
        self.progressBar.setValue(0.0193 * adc.read_adc(2, gain=GAIN) - 458.64)
        self.xbar.setValue(0.077 * adc.read_adc(0, gain=GAIN) - 1009.9)
        self.ybar.setValue(0.0771 * adc.read_adc(1, gain=GAIN) - 1016)
        data = [int(0.077 * adc.read_adc(0, gain=GAIN) - 1009.9), int(0.0771 * adc.read_adc(1, gain=GAIN) - 1016)]  
        clientsocket.send("walk" + pickle.dumps(data))
        # kijkt of percentage te laag is, dan kleur rood.
        if(0.0193 * adc.read_adc(2, gain=GAIN) - 458.64 < 20):
        	self.progressBar.setStyleSheet("QProgressBar{border: 2px solid grey;text-align: center}QProgressBar::chunk {background-color: red;width: 5px;margin: 1px;}")
        else:
       	     self.progressBar.setStyleSheet("")
             # Vangt joystick button af
        if (GPIO.input(INPUT_PIN) == True):            
 		self.RollButton.setText("Pick!")
        else:
            self.RollButton.setText("")
            # Sluit pi af bij percentage onder de 5%
        if(0.0193 * adc.read_adc(2, gain=GAIN) - 458.64 < 5):
	    #os.system("sudo shutdown -P now")
            print "Power Low"
    def total(self,total):
        self.progressBar.setMaximum(total)

    def ExitClick(self):
    	try:
    		clientsocket.send("exit")
    	except:
    		print "Socket not open"
    	self.close()

    def RollClick(self):
	self.FG = RollWindow()
	self.FG.show()

    def DansClick(self):
	self.FD = DansWindow()
	self.FD.show()

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
