from collections import deque
import imutils
import math
import time
import subprocess
import threading
import sys
import csv
import dynamixel
import collections

sys.path.insert(0, '/home/pi/spInDP/Spin/Loopscripts')

from walk_test import Walk
walk = Walk()

from classes.ik import IK

class Dance(object):

	def __init__(self):
		serial = dynamixel.SerialStream(port="/dev/USB2AX",
		baudrate="1000000",
		timeout=1)

		self.net = dynamixel.DynamixelNetwork(serial)

		servos = [32, 40, 41, 10, 11, 12, 61, 50, 51, 20, 21, 22, 62, 52, 60, 42, 30, 31]

		for servoId in servos:
			newDynamixel = dynamixel.Dynamixel(servoId, self.net)
			self.net._dynamixel_map[servoId] = newDynamixel

		self._previousTime = 0
		self._numTicks = 0
		self._servoUpdatePeriod = 20

		self._rot = 0
		self._x = 0
		self._y = 0
		self._r = 0
		self._Walk = False

		# self._WalkTest = threading.Thread(target=self.WalkTest)
		# self._WalkTest.start()


		self._ik = IK()
		self._ik.initInitialPositions()
		self._ik.bodyFK(0, 0, 0, 0, 0, 60)


	# def WalkTest(self):
	# 	while True:
	# 		while self._Walk:
	# 			currentTime = int(round(time.time() * 1000))

	# 			if currentTime - self._previousTime >= self._ik._servoUpdatePeriod:
	# 				self._previousTime = currentTime
	# 				self._ik.initTripod(self._x, self._y, self._r)
	# 				#self._ik.bodyFK(0, 0, 0, 0, 0, 0)

	def calculateNumTicks(self, duration):
		self._numTicks = duration / self._servoUpdatePeriod

	def smoothMotionRotX(self, cycle, value, tick, offset):
		return math.sin(math.radians(offset) + math.pi  * cycle * tick / self._numTicks) * value

	def smoothMotionRotY(self, cycle, value, tick, offset):
		return math.sin(math.radians(offset) + math.pi  * cycle * tick / self._numTicks) * value

	def smoothMotionRotZ(self, cycle, value, tick, offset):
		return -math.sin(math.radians(offset) + math.pi  * cycle * tick / self._numTicks) * value

	def smoothMotionTransX(self, cycle, value, tick, offset):
		return math.sin(math.radians(offset) + math.pi  * cycle * tick / self._numTicks) * value

	def smoothMotionTransY(self, cycle, value, tick, offset):
		return math.sin(math.radians(offset) + math.pi  * cycle * tick / self._numTicks) * value

	def smoothMotionTransZ(self, cycle, value, tick, offset):
		return math.sin(math.radians(offset) + math.pi  * cycle * tick / self._numTicks) * value

	def bodyFKX(self, times, xRotValue, yRotValue, zRotValue, xTransValue, yTransValue, zTransValue, duration, rotXCycle, rotYCycle, rotZCycle, transXCycle, transYCycle, transZCycle, offsetRotX, offsetRotY, offsetRotZ, offsetTransX, offsetTransY, offsetTransZ):
		self.calculateNumTicks(duration)
		for x in xrange(0, times):
			for tick in xrange(1, self._numTicks + 2):
				rotX = self.smoothMotionRotX(rotXCycle, xRotValue, tick, offsetRotX)
				rotY = self.smoothMotionRotY(rotYCycle, yRotValue, tick, offsetRotY)
				rotZ = self.smoothMotionRotZ(rotZCycle, zRotValue, tick, offsetRotZ)
				transX = self.smoothMotionTransX(transXCycle, xTransValue, tick, offsetTransX)
				transY = self.smoothMotionTransY(transYCycle, yTransValue, tick, offsetTransY)
				transZ = self.smoothMotionTransZ(transZCycle, zTransValue, tick, offsetTransZ)
				self._ik.bodyFK(rotX, rotY, rotZ, transX, transY, transZ)
				time.sleep(self._servoUpdatePeriod / 1000)


	def turnRight(self):
		startTime = time.time()
		currentTime = startTime
		while currentTime < startTime + 4.5:
			currentTime = time.time()
			self._ik.initTripod(0, 0, 1023)
			self._ik.bodyFK(0, 0, 0, 0, 0, 0)

	def turnLeft(self):
		startTime = time.time()
		currentTime = startTime
		while currentTime < startTime + 4.2:
			currentTime = time.time()
			self._ik.initTripod(0, 0, -1023)
			self._ik.bodyFK(0, 0, 0, 0, 0, 0)

	def walk(self, xValue, yValue):
		startTime = time.time()
		currentTime = startTime
		while currentTime < startTime + 4.2:
			currentTime = time.time()
			self._ik.initTripod(xValue, yValue, 0)
			self._ik.bodyFK(0, 0, 0, 0, 0, 0)

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

	def Dance(self):
		time.sleep(0.3)

		self._ik.bodyFK(0, 0, 0, 0, 0, 45)
		time.sleep(1.95)
		self._ik.bodyFK(0, 0, 0, 0, 0, 30)
		time.sleep(1.95)
		self._ik.bodyFK(0, 0, 0, 0, 0, 15)
		time.sleep(1.95)
		self._ik.bodyFK(0, 0, 0, 0, 0, 0)
		time.sleep(1.95)

		#move to all sides
		self.bodyFKX(1, 0, 0, 0, 75, 0, 0, 1950, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
		time.sleep(0.75)
		self.bodyFKX(1, 0, 0, 0, -75, 0, 0, 1950, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
		time.sleep(0.75)
		self.bodyFKX(1, 0, 0, 0, 0, -75, 0, 1950, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
		time.sleep(0.75)
		self.bodyFKX(1, 0, 0, 0, 0, 75, 0, 1600, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)

		#Clap
		self.runCSV("/home/pi/spInDP/Spin/Loopscripts/clapStart.csv")
		time.sleep(0.25)
		self.runCSV("/home/pi/spInDP/Spin/Loopscripts/clap.csv")
		time.sleep(0.5)
		self.runCSV("/home/pi/spInDP/Spin/Loopscripts/clap2.csv")
		time.sleep(0.5)
		self.runCSV("/home/pi/spInDP/Spin/Loopscripts/clap2.csv")
		time.sleep(0.5)
		self.runCSV("/home/pi/spInDP/Spin/Loopscripts/clap2.csv")
		time.sleep(0.5)
		self.runCSV("/home/pi/spInDP/Spin/Loopscripts/clapEnd.csv")
		time.sleep(0.85)

		#Turn Right
		self.turnRight()
		self._ik.initInitialPositions()
		self._ik.bodyFK(0, 0, 0, 0, 0, 0)
		time.sleep(0.2)

		#Turn Left
		self.turnLeft()
		self._ik.initInitialPositions()
		self._ik.bodyFK(0, 0, 0, 0, 0, 0)

		#Worm Y
		self.bodyFKX(1, 0, 20, 0, 0, 0, 0, 2000, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.bodyFKX(4, 0, 20, 0, 0, 0, 40, 1750, 0, 2, 0, 0, 0, 2, 0, 90, 0, 0, 0, 0)
		self.bodyFKX(1, 0, 20, 0, 0, 0, 0, 1750, 0, 1, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0)
		self.bodyFKX(4, 0, 20, 0, 0, 0, 40, 1750, 0, 2, 0, 0, 0, 2, 0, 270, 0, 0, 0, 0)
		self.bodyFKX(1, 20, 20, 0, 0, 0, 0, 1750, 0, 0.5, 0, 0, 0, 2, 0, 270, 0, 0, 0, 0)

		#Worm X
		self.bodyFKX(1, 20, 0, 0, 0, 0, 0, 2000, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.bodyFKX(4, 20, 0, 0, 0, 0, 40, 1750, 2, 0, 0, 0, 0, 2, 90, 0, 0, 0, 0, 0)
		self.bodyFKX(1, 20, 0, 0, 0, 0, 0, 1750, 1, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0)
		self.bodyFKX(4, 20, 0, 0, 0, 0, 40, 1750, 2, 0, 0, 0, 0, 2, 270, 0, 0, 0, 0, 0)
		self.bodyFKX(1, 20, 0, 0, 0, 0, 0, 1400, 0.5, 0, 0, 0, 0, 2, 270, 0, 0, 0, 0, 0)

		#move to all sides
		time.sleep(0.2)
		self.bodyFKX(1, 0, 0, 0, 75, 0, 0, 1950, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
		time.sleep(0.75)
		self.bodyFKX(1, 0, 0, 0, -75, 0, 0, 1950, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
		time.sleep(0.75)
		self.bodyFKX(1, 0, 0, 0, 0, -75, 0, 1700, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
		time.sleep(0.75)

		#Go Down
		self.bodyFKX(1, 0, 0, 15, 0, 0, 60, 3000, 0, 0, 2, 0, 0, 0.5, 0, 0, 0, 0, 0, 0)
		time.sleep(3)

		#Get Up
		self.bodyFKX(1, 0, 0, -15, 0, 0, 60, 3000, 0, 0, 2, 0, 0, 0.5, 0, 0, 0, 0, 0, 90)

		self.bodyFKX(1, 0, 0, 0, 50, 0, 0, 2000, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0)
		self.bodyFKX(3, 0, 0, 0, 50, 50, 0, 3000, 0, 0, 0, 2, 2, 0, 0, 0, 0, 90, 0, 0)
		#self.bodyFKX(1, 0, 0, 0, 50, 50, 0, 2000, 0, 0, 0, 0.5, 2, 0, 0, 0, 0, 90, 0, 0)
		#self.walk(512, 512)
		#self.walk(-512, -512)
		#self.bodyFKX(1, 0, 10, 0, 50, 0, 0, 2000, 0, 0.5, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0)
		self.bodyFKX(3, 10, 10, 0, 50, 50, 0, 4000, 2, 2, 0, 2, 2, 0, 180, 90, 0, 90, 0, 0)
		self.bodyFKX(1, 10, 10, 0, 50, 50, 0, 2000, 2, 0.5, 0, 0.5, 2, 0, 180, 90, 0, 90, 0, 0)

		#jump
		#self.bodyFKX(6, 0, 0, 0, 0, 0, 50, 500, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0)

		for i in range(0, 2):
			self.runCSV("/home/pi/spInDP/Spin/Loopscripts/wave.csv")
			time.sleep(0.2)
			self.runCSV("/home/pi/spInDP/Spin/Loopscripts/waveBack.csv")
			time.sleep(0.2)
			self.runCSV("/home/pi/spInDP/Spin/Loopscripts/wave2.csv")
			time.sleep(0.2)
			self.runCSV("/home/pi/spInDP/Spin/Loopscripts/waveBack2.csv")
			time.sleep(0.2)


		self.walk(256, 256)
		time.sleep(0.02)
		self.walk(-256, -256)
		time.sleep(0.02)
		self.walk(256, -256)
		time.sleep(0.02)
		self.walk(-256, 256)
		time.sleep(0.2)

		#jump
		self.bodyFKX(10, 0, 0, 0, 0, 0, 50, 500, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0)
		self.bodyFKX(1, 0, 0, 0, 0, 0, 60, 4000, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0)

dnce = Dance()
dnce.Dance()
