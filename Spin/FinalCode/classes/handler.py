import threading
import time
from walk import Walk

class Handler(object):

    def __init__(self, mode=1):
        self._Semaphore = threading.Semaphore(1)
        self._ExitSemaphore = threading.Semaphore(1)
        self._Exit = False

        if mode == 1:
            self._Walk = Walk()

    def runThread(self):
        self._ExitSemaphore.acquire()
        while not self._Exit:
            self._Walk.walk()
            #self._Mode.set_speed(1023)
            self._ExitSemaphore.release()
            time.sleep(0.001)

    def set_speed(self, x, y):
        self._Walk.set_speed(x, y)

    def Exit(self):
        self._ExitSemaphore.acquire()
        self._Exit = True
        self._ExitSemaphore.release()
