from classes.buffer import Buffer
from classes.server import Server
from classes.ik import IK

import classes.webservice
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

        self._IdleModeEnabled = False

        self._ik = IK()

        self._ServerThread = threading.Thread(target=self._Server.Start)
        self._ServerThread.start()
        self._CommandHandlerThread = threading.Thread(target=self.CommandHandler)
        self._CommandHandlerThread.start()
        self._WalkTest = threading.Thread(target=self.WalkTest)
        self._WalkTest.start()
        self._WebService = threading.Thread(target=classes.webservice.main)
        self._WebService.start()

    def CommandHandler(self):
        self._ik.initInitialPositions()
        self._ik.initTripod(0, 0, 0)
        self._ik.bodyFK(0, 0, 0, 0, 0, 0)

        while not self._Exit:

            data = self._Buffer.Pop()
            currentTime = int(round(time.time() * 1000))

            time1 = time.time()

            if len(str(data)) > 0:
                if "exit" in data:
                    #self.Exit()
                    #self._Exit = True
                    self._Mode = ""
                else:
                    print data
                    if "RotationEnable" in data:
                        self._RotationModeEnabled = True

                    if "RotationDisable" in data:
                        self._RotationModeEnabled = False

                    if "IdleMode" in data:
                        for i in range(90):
                            self._ik._rideHeight = 130 - i
                            self._ik.initInitialPositions()
                            self._ik.initTripod(0, 0, 0)
                            self._ik.bodyFK(0, 0, 0, 0, 0, 0)

                    if "KrabWalk" in data:
                        #self.CheckIdleModeEnabled()
                        self._ik.initInitialPositionsCrab()
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._Walk = True
                        self._ik.clearCaseSteps()

                    if "TripodWalk" in data:
                        #self.CheckIdleModeEnabled()
                        self._ik.initInitialPositions()
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._Walk = True
                        self._ik.clearCaseSteps()

                    if "RippleWalk" in data:
                        #self.CheckIdleModeEnabled()
                        self._ik.initInitialPositions()
                        self._RippleModeEnabled = True
                        self._TripodModeEnabled = False
                        self._Walk = True
                        self._ik.clearCaseSteps()

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
                        except EOFError:
                            print("DATA ERROR")
                        except ValueError:
                            print("DATA ERROR")

    def CheckIdleModeEnabled(self):
        if self._IdleModeEnabled:
            for i in range(90):
                self._ik._rideHeight = 30 + i
                self._ik.initInitialPositions()
                self._ik.initTripod(0, 0, 0)
                self._ik.bodyFK(0, 0, 0, 0, 0, 0)
            self._IdleModeEnabled = False

    def WalkTest(self):
        while True:
            while self._Walk:
                currentTime = int(round(time.time() * 1000))

                if currentTime - self._previousTime >= 20:
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

                    try:
                        if self._BalanceModeEnabled:
                            self._ik.bodyFK(self._rotX, self._rotY, self._rotZ, 0, 0, 0)
                        else:
                            self._ik.bodyFK(0, 0, 0, 0, 0, 0)
                    except AttributeError:
                        print "Error"
                    except IndexError:
                        print "Error"


    def Exit(self):
        #self._Server.Exit()
        print("Goodbye")


if __name__ == '__main__':
    main = Main()
