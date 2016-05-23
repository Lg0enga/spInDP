import time
import array
import math
import csv
import locale
import operator
import collections
locale.setlocale( locale.LC_ALL, 'nl_NL.UTF-8' )
from dxl.dxlchain import DxlChain
from ax12 import Ax12
ax12 = Ax12()

__author__ = 'Jelmer Visser'

class Walk:

    walk = True
    backwards = False
    crab = False

    speed = 1023

    def set_speed(self, y, x):
        if y < 0:
            self.backwards = True
        else:
            self.backwards = False

        if y == 0:
            self.crab = True
            if x < 0:
                self.backwards = True
            else:
                self.backwards = False
            y = x
        else:
            self.crab = False;

        y = abs(y)
        self.speed = y


    def degreesToBits(degrees):
        return int((1023 * degrees) / 300)

    def findServos(self):
        return ax12.learnServos()

    def setBeginPosition(self):
        ax12.moveSpeedRW(10, 512, 512)
        ax12.moveSpeedRW(11, 512, 512)
        ax12.moveSpeedRW(12, 512, 512)
        ax12.moveSpeedRW(20, 512, 512)
        ax12.moveSpeedRW(21, 512, 512)
        ax12.moveSpeedRW(22, 512, 512)
        ax12.moveSpeedRW(30, 512, 512)
        ax12.moveSpeedRW(31, 512, 512)
        ax12.moveSpeedRW(32, 512, 512)
        ax12.moveSpeedRW(40, 512, 512)
        ax12.moveSpeedRW(41, 512, 512)
        ax12.moveSpeedRW(42, 512, 512)
        ax12.moveSpeedRW(50, 512, 512)
        ax12.moveSpeedRW(51, 512, 512)
        ax12.moveSpeedRW(52, 512, 512)
        ax12.moveSpeedRW(60, 512, 512)
        ax12.moveSpeedRW(61, 512, 512)
        ax12.moveSpeedRW(62, 512, 512)

    def readTemperature(self):
        print ax12.readTemperature(10)
        print ax12.readTemperature(11)
        print ax12.readTemperature(12)
        print ax12.readTemperature(20)
        print ax12.readTemperature(21)
        print ax12.readTemperature(22)
        print ax12.readTemperature(30)
        print ax12.readTemperature(31)
        print ax12.readTemperature(32)
        print ax12.readTemperature(40)
        print ax12.readTemperature(41)
        print ax12.readTemperature(42)
        print ax12.readTemperature(50)
        print ax12.readTemperature(51)
        print ax12.readTemperature(52)
        print ax12.readTemperature(60)
        print ax12.readTemperature(61)
        print ax12.readTemperature(62)

    def straight(self):
    	ax12.moveSpeed(10, 512, 512)
    	ax12.moveSpeed(11, 512, 512)
    	ax12.moveSpeed(12, 512, 512)
    	ax12.moveSpeed(20, 512, 512)
    	ax12.moveSpeed(21, 512, 512)
    	ax12.moveSpeed(22, 512, 512)
    	ax12.moveSpeed(30, 512, 512)
    	ax12.moveSpeed(31, 512, 512)
    	ax12.moveSpeed(32, 512, 512)
    	ax12.moveSpeed(40, 512, 512)
    	ax12.moveSpeed(41, 512, 512)
    	ax12.moveSpeed(42, 512, 512)
    	ax12.moveSpeed(50, 512, 512)
    	ax12.moveSpeed(51, 512, 512)
    	ax12.moveSpeed(52, 512, 512)
    	ax12.moveSpeed(60, 512, 512)
    	ax12.moveSpeed(61, 512, 512)
    	ax12.moveSpeed(62, 512, 512)

    def setTorque(self, maxTorque):
    	ax12.setTorqueLimit(10, maxTorque)
    	ax12.setTorqueLimit(11, maxTorque)
    	ax12.setTorqueLimit(12, maxTorque)
    	ax12.setTorqueLimit(20, maxTorque)
    	ax12.setTorqueLimit(21, maxTorque)
    	ax12.setTorqueLimit(22, maxTorque)
    	ax12.setTorqueLimit(30, maxTorque)
    	ax12.setTorqueLimit(31, maxTorque)
    	ax12.setTorqueLimit(32, maxTorque)
    	ax12.setTorqueLimit(40, maxTorque)
    	ax12.setTorqueLimit(41, maxTorque)
    	ax12.setTorqueLimit(42, maxTorque)
    	ax12.setTorqueLimit(50, maxTorque)
    	ax12.setTorqueLimit(51, maxTorque)
    	ax12.setTorqueLimit(52, maxTorque)
    	ax12.setTorqueLimit(60, maxTorque)
    	ax12.setTorqueLimit(61, maxTorque)
    	ax12.setTorqueLimit(62, maxTorque)

    def setReturnDelayTime(self):
        ax12.setReturnDelayTime(10, 100)
        ax12.setReturnDelayTime(11, 100)
        ax12.setReturnDelayTime(12, 100)
        ax12.setReturnDelayTime(20, 100)
        ax12.setReturnDelayTime(21, 100)
        ax12.setReturnDelayTime(22, 100)
        ax12.setReturnDelayTime(30, 100)
        ax12.setReturnDelayTime(31, 100)
        ax12.setReturnDelayTime(32, 100)
        ax12.setReturnDelayTime(40, 100)
        ax12.setReturnDelayTime(41, 100)
        ax12.setReturnDelayTime(42, 100)
        ax12.setReturnDelayTime(50, 100)
        ax12.setReturnDelayTime(51, 100)
        ax12.setReturnDelayTime(52, 100)
        ax12.setReturnDelayTime(60, 100)
        ax12.setReturnDelayTime(61, 100)
        ax12.setReturnDelayTime(62, 100)

    def getReturnDelayTime(self):
        print ax12.readReturnDelayTime(10)
        print ax12.readReturnDelayTime(11)
        print ax12.readReturnDelayTime(12)
        print ax12.readReturnDelayTime(20)
        print ax12.readReturnDelayTime(21)
        print ax12.readReturnDelayTime(22)
        print ax12.readReturnDelayTime(30)
        print ax12.readReturnDelayTime(31)
        print ax12.readReturnDelayTime(32)
        print ax12.readReturnDelayTime(40)
        print ax12.readReturnDelayTime(41)
        print ax12.readReturnDelayTime(42)
        print ax12.readReturnDelayTime(50)
        print ax12.readReturnDelayTime(51)
        print ax12.readReturnDelayTime(52)
        print ax12.readReturnDelayTime(60)
        print ax12.readReturnDelayTime(61)
        print ax12.readReturnDelayTime(62)

    def doFactoryReset(self):
        ax12.factoryReset(10, True)
        time.sleep(1)
        ax12.setID(1, 10)
        time.sleep(1)
        ax12.factoryReset(11, True)
        time.sleep(1)
        ax12.setID(1, 11)
        time.sleep(1)
        ax12.factoryReset(12, True)
        time.sleep(1)
        ax12.setID(1, 12)
        time.sleep(1)
        ax12.factoryReset(20, True)
        time.sleep(1)
        ax12.setID(1, 20)
        time.sleep(1)
        ax12.factoryReset(21, True)
        time.sleep(1)
        ax12.setID(1, 21)
        time.sleep(1)
        ax12.factoryReset(22, True)
        time.sleep(1)
        ax12.setID(1, 22)
        time.sleep(1)
        ax12.factoryReset(30, True)
        time.sleep(1)
        ax12.setID(1, 30)
        time.sleep(1)
        ax12.factoryReset(31, True)
        time.sleep(1)
        ax12.setID(1, 31)
        time.sleep(1)
        ax12.factoryReset(32, True)
        time.sleep(1)
        ax12.setID(1, 32)
        time.sleep(1)
        ax12.factoryReset(40, True)
        time.sleep(1)
        ax12.setID(1, 40)
        time.sleep(1)
        ax12.factoryReset(41, True)
        time.sleep(1)
        ax12.setID(1, 41)
        time.sleep(1)
        ax12.factoryReset(42, True)
        time.sleep(1)
        ax12.setID(1, 42)
        time.sleep(1)
        ax12.factoryReset(50, True)
        time.sleep(1)
        ax12.setID(1, 50)
        time.sleep(1)
        ax12.factoryReset(51, True)
        time.sleep(1)
        ax12.setID(1, 51)
        time.sleep(1)
        ax12.factoryReset(52, True)
        time.sleep(1)
        ax12.setID(1, 52)
        time.sleep(1)
        ax12.factoryReset(60, True)
        time.sleep(1)
        ax12.setID(1, 60)
        time.sleep(1)
        ax12.factoryReset(61, True)
        time.sleep(1)
        ax12.setID(1, 61)
        time.sleep(1)
        ax12.factoryReset(62, True)
        time.sleep(1)
        ax12.setID(1, 62)
        time.sleep(1)
        self.setReturnDelayTime()

    def beginPosition(self):
        while True:
            while self.walk:

                csvFile = "/home/pi/spInDP/Spin/Loopscripts/walk_forward.csv"

                if self.backwards:
                    csvFile = "/home/pi/spInDP/Spin/Loopscripts/walk_backwards.csv"

                if self.crab:
                    csvFile = "/home/pi/spInDP/Spin/Loopscripts/crab_left.csv"
                    if self.backwards:
                        csvFile = "/home/pi/spInDP/Spin/Loopscripts/crab_right.csv"

                with open('%s' % csvFile, 'rb') as f:
                    records = csv.DictReader(f, delimiter=';')

                    maxValue = None

                    oldPositions = {}

                    try:
                        for row in records:

                            chain=DxlChain("/dev/ttyACM0",rate=1000000)
                            motors=chain.get_motor_list()

                            newPositions = {}
                            currentPositions = {}
                            deltaPositions = {}
                            finalPositions = {}
                            if self.walk:
                                for servo, position in list(row.items()):
                                    if not bool(oldPositions):
                                        currentPositions[servo] = chain.get_position((int(servo)))[int(servo)]
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
                                    chain.goto(int(servo),int(position_speed[0]),speed=int(position_speed[1]), blocking=False)

                                while chain.is_moving():
                                    print chain.get_position()

                                #time.sleep(float(1023 / self.speed) * (maxValue / float(205) * float((float(self.speed + 2069)) / 25767)))

                                oldPositions = newPositions
                    except Ax12.axError:
                        print("error")

    def oldBeginPosition(self):
        chain=DxlChain("/dev/ttyACM0",rate=1000000)
        motors=chain.get_motor_list()
        with open('IK_Update__10052016_old.csv', 'rb') as f:
            records = csv.DictReader(f, delimiter=';')

            for row in records:
                for servo, position in list(row.items()):
                    chain.goto(int(servo), int(position), speed=1023, blocking=False)

            while chain.is_moving():
                print chain.get_position()

    def stop(self):
        #print("stop")
        self.walk = False

    def start(self):
        #print("start")
        self.walk = True
