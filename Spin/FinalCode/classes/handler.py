import threading
import time
from walk import Walk

class Handler(object):

    def __init__(self, mode=1):
        self._Exit = False

        if mode == 1:
            self._Walk = Walk()

    def runThread(self):
        while not self._Exit:
            self._Walk.walk()

    def exit(self):
        self._Exit = True
