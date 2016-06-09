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

        self._previousTime = 0

        self._x = 0
        self._y = 0

        self._rotX = 0
        self._rotY = 0
        self._rotZ = 0

        self._TripodModeEnabled = False
        self._RippleModeEnabled = False
        self._BalanceModeEnabled = False
        self._RotationModeEnabled = False

        self._Walk = False

        self._ik = IK()

        self._ServerThread = threading.Thread(target=self._Server.Start)
        self._ServerThread.start()
        self._CommandHandlerThread = threading.Thread(target=self.CommandHandler)
        self._CommandHandlerThread.start()
        self._WalkTest = threading.Thread(target=self.WalkTest)
        self._WalkTest.start()

    def CommandHandler(self):
        self._ik.initInitialPositions()

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
                    if "RotationEnabled" in data:
                        print "RotationEnabled"
                        self._RotationModeEnabled = True

                    if "RotationDisabled" in data:
                        print "RotationDisabled"
                        self._RotationModeEnabled = False

                    if "TripodWalk" in data:
                        print "TripodWalk"
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._Walk = False

                    if "RippleWalk" in data:
                        print "RippleWalk"
                        self._RippleModeEnabled = True
                        self._TripodModeEnabled = False
                        self._Walk = False

                    if "data" in data:
                        data = data.replace("data", "")

                        try:
                            data_arr = cPickle.loads(data)

                            x = int(data_arr[0])
                            y = int(data_arr[1])

                            self._x = x
                            self._y = y

                        except cPickle.UnpicklingError:
                            print("DATA ERROR")

    def WalkTest(self):
        while self._Walk:
            currentTime = int(round(time.time() * 1000))

            if currentTime - self._previousTime >= self._ik._servoUpdatePeriod:
                self._previousTime = currentTime

                if self._TripodModeEnabled:
                    if self._RotationModeEnabled:
                        self._ik.initTripod(self._y, 0, self._x)
                    else:
                        self._ik.initTripod(self._y, self._x, 0)
                elif self._RippleModeEnabled:
                    if self._RotationModeEnabled:
                        self._ik.initRipple(self._y, 0, self._x)
                    else:
                        self._ik.initRipple(self._y, self._x, 0)

                if self._BalanceModeEnabled:
                    self._ik.bodyFK(self._rotX, self._rotY, self._rotZ, 0, 0, 0)
                else:
                    self._ik.bodyFK(0, 0, 0, 0, 0, 0)


    def Exit(self):
        self._Server.Exit()
        print("Goodbye")


if __name__ == '__main__':
    main = Main()
