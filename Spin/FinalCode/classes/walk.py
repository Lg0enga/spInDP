import os
import dynamixel
import sys
import subprocess
import optparse
import yaml
import csv
import collections
import time

servoList = None

class Walk:

    def __init__(self):
        self.walk = True
        self.backwards = False
        self.crab = False

        self.speed = 1023

        serial = dynamixel.SerialStream(port="/dev/USB2AX",
                                        baudrate="1000000",
                                        timeout=1)

        self.net = dynamixel.DynamixelNetwork(serial)

        servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

        for servoId in servos:
            newDynamixel = dynamixel.Dynamixel(servoId, self.net)
            self.net._dynamixel_map[servoId] = newDynamixel

    def SetSpeed(self, x, y):
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

        if self.speed > 1023:
            self.speed = 1023

    def Walk(self):
        while True:
            if self.speed > 100:

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

    def IsMoving(self, finalPositions):
        while True:
            rangeMin = int(finalPositions.items()[0][1][0]) - 15
            rangeMax = int(finalPositions.items()[0][1][0]) + 15

            if rangeMin < self.net._dynamixel_map[10].current_position < rangeMax:
                return False
            return True

    def Stop(self):
        self.speed = 0
