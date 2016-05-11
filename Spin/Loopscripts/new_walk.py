import time
import array
import math
import csv
import locale
import operator
import collections
locale.setlocale( locale.LC_ALL, 'nl_NL.UTF-8' )
from ax12 import Ax12
ax12 = Ax12()

__author__ = 'Jelmer Visser'

class Walk:

    walk = True

    speed = 1023
    x = 150
    y = 150
    z = 60
    z1 = 20
    CL = 53
    FL = 83
    TL = 126

    def set_speed(self, speed):
        self.speed = speed


    def degreesToBits(degrees):
        return int((1023 * degrees) / 300)

    def findServos(self):
        return ax12.learnServos()

    def setBeginPosition(self):
        print ax12.moveSpeedRW(10, 512, 512)
    	print ax12.moveSpeedRW(11, 512, 512)
    	print ax12.moveSpeedRW(12, 512, 512)
    	print ax12.moveSpeedRW(20, 512, 512)
    	print ax12.moveSpeedRW(21, 512, 512)
    	print ax12.moveSpeedRW(22, 512, 512)
    	print ax12.moveSpeedRW(30, 512, 512)
    	print ax12.moveSpeedRW(31, 512, 512)
    	print ax12.moveSpeedRW(32, 512, 512)
    	print ax12.moveSpeedRW(40, 512, 512)
    	print ax12.moveSpeedRW(41, 512, 512)
    	print ax12.moveSpeedRW(42, 512, 512)
    	print ax12.moveSpeedRW(50, 512, 512)
    	print ax12.moveSpeedRW(51, 512, 512)
    	print ax12.moveSpeedRW(52, 512, 512)
    	print ax12.moveSpeedRW(60, 512, 512)
    	print ax12.moveSpeedRW(61, 512, 512)
    	print ax12.moveSpeedRW(62, 512, 512)

    def readVoltage(self):
        print ax12.readVoltage(10)
        print ax12.readVoltage(11)
        print ax12.readVoltage(12)
        print ax12.readVoltage(20)
        print ax12.readVoltage(21)
        print ax12.readVoltage(22)
        print ax12.readVoltage(30)
        print ax12.readVoltage(31)
        print ax12.readVoltage(32)
        print ax12.readVoltage(40)
        print ax12.readVoltage(41)
        print ax12.readVoltage(42)
        print ax12.readVoltage(50)
        print ax12.readVoltage(51)
        print ax12.readVoltage(52)
        print ax12.readVoltage(60)
        print ax12.readVoltage(61)
        print ax12.readVoltage(62)

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

    def not_straight(self):
    	ax12.moveSpeed(10, 600, 2047)
    	ax12.moveSpeed(11, 600, 2047)
    	ax12.moveSpeed(12, 600, 2047)
    	ax12.moveSpeed(20, 600, 2047)
    	ax12.moveSpeed(21, 600, 2047)
    	ax12.moveSpeed(22, 600, 2047)
    	ax12.moveSpeed(30, 600, 2047)
    	ax12.moveSpeed(31, 600, 2047)
    	ax12.moveSpeed(32, 600, 2047)
    	ax12.moveSpeed(40, 600, 2047)
    	ax12.moveSpeed(41, 600, 2047)
    	ax12.moveSpeed(42, 600, 2047)
    	ax12.moveSpeed(50, 600, 2047)
    	ax12.moveSpeed(51, 600, 2047)
    	ax12.moveSpeed(52, 600, 2047)
    	ax12.moveSpeed(60, 600, 2047)
    	ax12.moveSpeed(61, 600, 2047)
    	ax12.moveSpeed(62, 600, 2047)

    def beginPosition(self):
        # while True:
            with open('IK_Update__11052016.csv', 'rb') as f:
                records = csv.DictReader(f, delimiter=';')

                maxValue = None

                for row in records:

                    newPositions = {}
                    currentPositions = {}
                    deltaPositions = {}
                    finalPositions = {}

                    for servo, position in row.items():
                        currentPositions[servo] = ax12.readPosition(int(servo))
                        newPositions[servo] = position

                    for servo, position in newPositions.items():
                        if int(currentPositions[servo]) - int(position) == 0:
                            deltaPositions[servo] = 1
                        else:
                            deltaPositions[servo] = abs(int(currentPositions[servo]) - int(position))

                    for servo, position in deltaPositions.items():
                        maxValue = max(deltaPositions.values())
                        finalPositions[servo] = newPositions[servo], int(float(deltaPositions[servo]) / float(maxValue) * self.speed)

                    finalPositions = collections.OrderedDict(sorted(finalPositions.items()))

                    for servo, position_speed in finalPositions.items():
                        ax12.moveSpeed(int(servo), int(position_speed[0]), int(position_speed[1]))

                    time.sleep(maxValue / float(205) * float(0.2))


    def oldBeginPosition(self):
        with open('IK_Update__10052016_old.csv', 'rb') as f:
            records = csv.DictReader(f, delimiter=';')

            for row in records:
                for servo, position in row.items():
                    ax12.moveSpeed(int(servo), int(position), 1023)

    def walk(self):
        with open('IK_Update__09052016.csv', 'rb') as f:
            reader = csv.reader(f, delimiter=';')
            data_as_list = list(reader)

        index = 0

        while True:
            for item in data_as_list:
                if index > 0:
                    ax12.moveSpeed(20, int(item[0]), int(float(item[3]) * self.speed))
                    ax12.moveSpeed(21, int(item[1]), int(float(item[4]) * self.speed))
                    ax12.moveSpeed(22, int(item[2]), int(float(item[5]) * self.speed))

                    ax12.moveSpeed(50, int(item[0]), int(float(item[3]) * self.speed))
                    ax12.moveSpeed(51, int(item[1]), int(float(item[4]) * self.speed))
                    ax12.moveSpeed(52, int(item[2]), int(float(item[5]) * self.speed))

                    time.sleep(locale.atof(item[6]) / self.speed)

                if index == 5:
                    index = 0
                else:
                    index += 1

    def stop(self):
        print "stop"
        self.walk = False
