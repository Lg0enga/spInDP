import threading
import time
from walk import Walk
from bodyik import BodyIK

class Handler(object):

    def __init__(self, mode=1):
        self._Semaphore = threading.Semaphore(1)
        self._ExitSemaphore = threading.Semaphore(1)
        self._Exit = False

        self._ModeID = mode
        # if mode == 1:
        #     self._Mode = Walk()
        #if mode == 2:
            #self._Mode = BodyIK()

    def runThread(self):
        self._ExitSemaphore.acquire()
        while not self._Exit:

            # if(self._ModeID == 1):
            #     self._Mode.Walk()

            #self._Mode.set_speed(1023)
            self._ExitSemaphore.release()
            time.sleep(0.001)

    def set_speed(self, x, y):
        self._Walk.SetSpeed(x, y)

    def BodyIK(self, x, y):
        self._Mode.BodyIK(x, y)

    def SetInitialValues(self):
        self._Mode.SetInitialValues()

    def Exit(self):
        self._ExitSemaphore.acquire()
        self._Exit = True
        self._ExitSemaphore.release()
