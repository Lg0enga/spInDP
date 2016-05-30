
from PyQt4 import QtCore, QtGui, uic
import sys, time


qtCreatorFile = "home.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class mythread(QtCore.QThread):
    def __init__(self,parent,n):
        QtCore.QThread.__init__(self,parent) 
        self.n=n

    def run(self):
        self.emit(QtCore.SIGNAL("total(PyQt_PyObject)"),self.n)
        i=0
        while (i<self.n):            
            self.emit(QtCore.SIGNAL("update()"))
            time.sleep(1)

# create the dialog for zoom to point
class progress(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self): 
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.t=mythread(self,100)
        QtCore.QObject.connect(self.t, QtCore.SIGNAL("total(PyQt_PyObject)"), self.total)
        QtCore.QObject.connect(self.t, QtCore.SIGNAL("update()"), self.update)
        self.n=0
        self.t.start()
    def update(self):
        self.n+=1
        print self.n
        self.progressBar.setValue(self.n)
    def total(self,total):
        self.progressBar.setMaximum(total)

if __name__=="__main__":
    app = QtGui.QApplication([])
    c=progress()
    c.show()
    sys.exit(app.exec_())