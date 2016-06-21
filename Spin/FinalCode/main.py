from classes.buffer import Buffer
from classes.server import Server
from classes.ik import IK
from classes.gyro_MPU import GyroData
from test_drive import DriveServos

import Adafruit_PCA9685
import classes.webservice
import time
import threading
import subprocess
import cPickle
import sys
import subprocess, signal
import time
import csv
import dynamixel
import collections

pwm = Adafruit_PCA9685.PCA9685()

class Main(object):
    def __init__(self):
        serial = dynamixel.SerialStream(port="/dev/USB2AX",
        baudrate="1000000",
        timeout=1)

        self.net = dynamixel.DynamixelNetwork(serial)

        servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

        for servoId in servos:
            newDynamixel = dynamixel.Dynamixel(servoId, self.net)
            self.net._dynamixel_map[servoId] = newDynamixel

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
        self._CrabModeEnabled = False
        self._BalanceModeEnabled = False
        self._RotationModeEnabled = False
        self._DriveModeEnabled = False
        self._VisionEnabled = False

        self._Walk = False

        self._IdleModeEnabled = False

        self._ik = IK()
        self._ds = DriveServos()
        self._gyro = GyroData()
        self._gyro.getGyroDataX(0)
        self._gyro.getGyroDataY(0)

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

        while not self._Exit and not self._VisionEnabled:

            data = self._Buffer.Pop()
            currentTime = int(round(time.time() * 1000))

            time1 = time.time()

            if len(str(data)) > 0:
                if "exit" in data:
                    #self.Exit()
                    #self._Exit = True
                    self._Mode = ""
                else:
                    if "StartDance" in data:
                        self._VisionEnabled = True
                        # dance = Dance()
                        # self._Dance = threading.Thread(target=dance.Dance())
                        # self._Dance.start()
                        # break

                    if "RotationEnable" in data:
                        self._RotationModeEnabled = True
                        if self._CrabModeEnabled:
                            self._ik.initInitialPositionsCrab(True)

                    if "RotationDisable" in data:
                        self._RotationModeEnabled = False
                        if self._CrabModeEnabled:
                            self._ik.initInitialPositionsCrab(False)

                    if "IdleMode" in data:
                        for i in range(70):
                            height = 0
                            self._ik.initTripod(0, 0, 0)
                            self._ik.bodyFK(0, 0, 0, 0, 0, height)
                            height += i

                    if "BalanceEnabled" in data:
                        self._BalandeModeEnabled = True

                    if "BalanceEnabled" in data:
                        self._BalandeModeEnabled = False

                    if "KrabWalk" in data:
                        #self.CheckIdleModeEnabled()
                        if self._RotationModeEnabled:
                            self._ik.initInitialPositionsCrabNew(True)
                        else:
                            self._ik.initInitialPositionsCrabNew(False)

                        self._CrabModeEnabled = True
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._Walk = True
                        self._BalandeModeEnabled = False
                        self._ik.clearCaseSteps()

                    if "DriveModeEnabled" in data:
                        self.runCSV("/home/pi/spInDP/Spin/Loopscripts/drive.csv")
                        time.sleep(1)
                        self._TripodModeEnabled = False
                        self._RippleModeEnabled = False
                        self._CrabModeEnabled = False
                        self._Walk = False
                        self._BalandeModeEnabled = False
                        self._DriveModeEnabled = True

                    if "DriveModeDisabled" in data:
                        self.runCSV("/home/pi/spInDP/Spin/Loopscripts/drive_back.csv")
                        time.sleep(1)
                        self._DriveModeEnabled = False
                        self._Walk = True

                    if "GrindWalk" in data:
                        self._ik.initInitialPositionsGrindbak()
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._CrabModeEnabled = False
                        self._Walk = True
                        self._BalandeModeEnabled = False
                        self._ik.clearCaseSteps()

                    if "SprintWalk" in data:
                        self._ik.initInitialPositionsRace()
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._CrabModeEnabled = False
                        self._Walk = True
                        self._BalandeModeEnabled = False
                        self._ik.clearCaseSteps()

                    if "TripodWalk" in data:
                        #self.CheckIdleModeEnabled()
                        self._ik.initInitialPositions()
                        self._TripodModeEnabled = True
                        self._RippleModeEnabled = False
                        self._CrabModeEnabled = False
                        self._Walk = True
                        self._BalandeModeEnabled = False
                        self._ik.clearCaseSteps()

                    if "RippleWalk" in data:
                        #self.CheckIdleModeEnabled()
                        self._ik.initInitialPositions()
                        self._RippleModeEnabled = True
                        self._TripodModeEnabled = False
                        self._CrabModeEnabled = False
                        self._Walk = True
                        self._BalandeModeEnabled = False
                        self._ik.clearCaseSteps()

                    if "PaarDance" in data:
                        self._Walk = False
                        self.runCSV("/home/pi/spInDP/Spin/Loopscripts/prik_paring.csv")
                        self._Walk = True

                    if "FuryRoad" in data:
                        self._VisionEnabled = True
                        #pwm.set_pwm(9, 0, 4095)
                        # fr = FuryRoad()
                        # self._FuryRoad = threading.Thread(target=fr.detectFuryroad)
                        # self._FuryRoad.start()
                        #self.KillThreads()

                    if "AutonoomBalloon" in data:
                        self._VisionEnabled = True
                        # ab = Vision()
                        # self._BalloonTracking = threading.Thread(target=ab.displayScreen)
                        # self._BalloonTracking.start()
                        #self.KillThreads()

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

                    if "led" in data:
                        data = data.replace("led", "")
                        try:
                            data_arr = cPickle.loads(data)
                            r = int(data_arr[0])
                            g = int(data_arr[1])
                            b = int(data_arr[2])

                            pwm.set_pwm(13, 0, r)
                            pwm.set_pwm(7, 0, r)
                            pwm.set_pwm(11, 0, r)
                            pwm.set_pwm(4, 0, g)
                            pwm.set_pwm(6, 0, g)
                            pwm.set_pwm(12, 0, g)
                            pwm.set_pwm(8, 0, b)
                            pwm.set_pwm(10, 0, b)
                            pwm.set_pwm(5, 0, b)
                        except cPickle.UnpicklingError:
                            print("DATA ERROR")
                        except EOFError:
                            print("DATA ERROR")
                        except ValueError:
                            print("DATA ERROR")
                        except IndexError:
                            print("No index")


    def CheckIdleModeEnabled(self):
        if self._IdleModeEnabled:
            for i in range(90):
                self._ik._rideHeight = 30 + i
                self._ik.initInitialPositions()
                self._ik.initTripod(0, 0, 0)
                self._ik.bodyFK(0, 0, 0, 0, 0, 0)
            self._IdleModeEnabled = False

    def KillThreads(self):
        self._ServerThread.join()
        self._CommandHandlerThread.join()
        self._WalkTest.join()

    def WalkTest(self):
        while not self._Exit and not self._VisionEnabled:

            while self._DriveModeEnabled:
                self._ds.drive(self._x, self._y)

            while self._Walk:
                currentTime = int(round(time.time() * 1000))

                if currentTime - self._previousTime >= 20:
                    self._previousTime = currentTime

                    if self._y > 1023:
                        self._y = 1023

                    if self._x > 1023:
                        self._x = 1023

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

    def runCSV(self, csvName):
		csvFile = csvName

		self.speed = 1023

		with open('%s' % csvFile, 'rb') as f:
		    records = csv.DictReader(f, delimiter=';')

		    maxValue = None

		    oldPositions = {}

		    index = 0

		    for row in records:

		        newPositions = {}
		        currentPositions = {}
		        deltaPositions = {}
		        finalPositions = {}

		        for servo, position in list(row.items()):
		            if not bool(oldPositions):
		                currentPositions[servo] = self.net._dynamixel_map[int(servo)].current_position
		            else:
		                currentPositions[servo] = oldPositions[servo]

		            newPositions[servo] = position

		        for servo, position in list(newPositions.items()):
		            if int(currentPositions[servo]) - int(position) == 0:
		                deltaPositions[servo] = 1
		            else:
		                deltaPositions[servo] = abs(int(currentPositions[servo]) - int(position))

		        for servo, position in list(deltaPositions.items()):
		            maxValue = max(deltaPositions.values())
		            finalPositions[servo] = newPositions[servo], int(float(deltaPositions[servo]) / float(maxValue) * self.speed)

		        finalPositions = collections.OrderedDict(sorted(finalPositions.items()))

		        for servo, position_speed in list(finalPositions.items()):
		            actuator = self.net._dynamixel_map[int(servo)]
		            actuator.moving_speed = int(position_speed[1])
		            actuator.goal_position = int(position_speed[0])

		        self.net.synchronize()
		        index += 1

		        time.sleep(float(1023 / self.speed) * (maxValue / float(205) * float((float(self.speed + 2069)) / 25767)))

		        oldPositions = newPositions


if __name__ == '__main__':
    main = Main()
