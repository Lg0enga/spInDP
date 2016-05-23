import threading
from threading import Semaphore

class Buffer(object):

    def __init__(self):
        self._Buffer = []
        self._BufferSemaphore = threading.Semaphore(1)

    def Stack(self, obj):
        self._BufferSemaphore.acquire()
        self._Buffer.append(obj)
        self._BufferSemaphore.release()

    def Pop(self):
        self._BufferSemaphore.acquire()

        output = ""
        try:
            output = self._Buffer.pop()
        except:
            output = ""

        self._BufferSemaphore.release()

        return output
