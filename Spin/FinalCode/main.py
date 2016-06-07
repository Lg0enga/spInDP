from classes.buffer import Buffer
from classes.server import Server
from classes.ik import IK

import time
import threading
import subprocess
import cPickle
import sys
import subprocess, signal
import time

class Main(object):
    def __init__(self):
        self._Buffer = Buffer()
        self._Server = Server(self._Buffer)
        self._Exit = False

        self._ServerThread = threading.Thread(target=self._Server.Start)
        self._ServerThread.start()
        self._CommandHandlerThread = threading.Thread(target=self.CommandHandler)
        self._CommandHandlerThread.start()

        self._ik = IK()
        self._ik.initInitialPositions()

        self._previousTime = 0

        self._x = 0
        self._y = 0

        self._Mode = ""

    def CommandHandler(self):
        while not self._Exit:

            data = self._Buffer.Pop()
            currentTime = int(round(time.time() * 1000))

            time1 = time.time()

            if len(str(data)) > 0:
                if "exit" in data:
                    self.Exit()
                    self._Exit = True
                    self._Mode = ""
                else:
                    print data

                    data = data.replace("walk", "")

                    try:
                        data_arr = cPickle.loads(data)

                        x = int(data_arr[0])
                        y = int(data_arr[1])

                        self._x = x
                        self._y = y

                        currentTime = int(round(time.time() * 1000))

                        if currentTime - self._previousTime >= self._ik._servoUpdatePeriod:
                            self._previousTime = currentTime

                            self._ik.initTripod(self._y, self._x, 0)
                            self._ik.bodyFK(0, 0, 0, 0, 0, 0)

                    except cPickle.UnpicklingError:
                        print("DATA ERROR")
                    # if "NormalWalk" in data:
                    #     self._Mode = "NormalWalk"
                    # elif "prik" in data:
                    #     self._Mode = "Prik"
                    #
                    # if self._Mode == "NormalWalk":
                    #     data = data.replace("walk", "")
                    #
                    #     try:
                    #         data_arr = cPickle.loads(data)
                    #
                    #         x = int(data_arr[0])
                    #         y = int(data_arr[1])
                    #
                    #         self._x = x
                    #         self._y = y
                    #
                    #         currentTime = int(round(time.time() * 1000))
                    #
                    #         if currentTime - self._previousTime >= self._ik._servoUpdatePeriod:
                    #             self._previousTime = currentTime
                    #
                    #             ik.initTripod(self._y, self._x, 0)
                    #             ik.bodyFK(0, 0, 0, 0, 0, 0)
                    #
                    #     except cPickle.UnpicklingError:
                    #         print("DATA ERROR")


    def Exit(self):
        self._Server.Exit()
        print("Goodbye")


if __name__ == '__main__':
    main = Main()
