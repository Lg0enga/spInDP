import threading
import time
from walk import Walk
from bodyik import BodyIK
from ik import IK

class Handler(object):

    def __init__(self, mode=1):
        self._Semaphore = threading.Semaphore(1)
        self._ExitSemaphore = threading.Semaphore(1)
        self._Exit = False
        self._previousTime = 0
        self._y = 0
        self._x = 0

        self._ModeID = mode
        if mode == 1:
            self._Mode = IK()
            self._Mode.initInitialPositions()
        #if mode == 2:
            #self._Mode = BodyIK()

    def runThread(self):
        self._ExitSemaphore.acquire()
        while not self._Exit:

            #self._Mode.set_speed(1023)
            self._ExitSemaphore.release()
            time.sleep(0.001)

    def set_speed(self, x, y):
        currentTime = int(round(time.time() * 1000))

        if currentTime - self._previousTime >= self._Mode._servoUpdatePeriod:
            self._previousTime = currentTime

            self._Mode.initTripod(y, x, 0)
            self._Mode.bodyFK(0, 0, 0, 0, 0, 0)

    def prik(self):
        self._Mode.Prik()

    def BodyIK(self, x, y):
        self._Mode.BodyIK(x, y)

    def SetInitialValues(self):
        self._Mode.SetInitialValues()

    def Exit(self):
        self._ExitSemaphore.acquire()
        self._Exit = True
        self._ExitSemaphore.release()

    def StopWalk(self):
        self._Mode.Stop()

    def StartWalk(self):
        self._Mode.Start()
