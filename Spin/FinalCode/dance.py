from collections import deque 
import imutils 
import time
import subprocess
import threading
import sys

sys.path.insert(0, '/home/pi/spInDP/Spin/Loopscripts')

from walk_test import Walk
walk = Walk()

from classes.ik import IK

class Dance(object):

	def __init__(self):
		self._previousTime = 0
		self._duration = 260
		self._tick = 20
		self._x = 0
        	self._y = 0
        	self._r = 0
		self._Walk = False		

		# self._WalkTest = threading.Thread(target=self.WalkTest)
		# self._WalkTest.start()

		self._ik = IK()
		self._ik.initInitialPositions()
		self._ik.bodyFK(0, 0, 0, 0, 0, 0)


	# def WalkTest(self):
	# 	while True:
	# 		while self._Walk:
	# 			currentTime = int(round(time.time() * 1000))

	# 			if currentTime - self._previousTime >= self._ik._servoUpdatePeriod:
	# 				self._previousTime = currentTime
	# 				self._ik.initTripod(self._x, self._y, self._r)
	# 				#self._ik.bodyFK(0, 0, 0, 0, 0, 0)
	
	#def sinus(self):

	def bodyFKX(self, times, maxX):
		xIteration = maxX/5
		xValue = 0
		for x in xrange(0,times):
			for i in xrange(0,xIteration):
				if x > 0:
					xValue += 5
				self._ik.bodyFK(xValue,0,0,0,0,0)
				time.sleep(0.05)
				if x == 0:
					xValue += 5 
			for i in xrange(0,xIteration*2):
				xValue -= 5
				self._ik.bodyFK(xValue,0,0,0,0,0)
				time.sleep(0.05)
			for i in xrange(0,xIteration):
				xValue += 5
				self._ik.bodyFK(xValue,0,0,0,0,0)
				time.sleep(0.05)

	# def bodyFKX(self, times, maxX):
	# 	xIteration = maxX/5
	# 	xValue = 0
	# 	for x in xrange(0,times):
	# 		for i in xrange(0,xIteration):
	# 			if x > 0:
	# 				xValue += 5
	# 			self._ik.bodyFK(xValue,0,0,0,0,0)
	# 			time.sleep(0.05)
	# 			if x == 0:
	# 				xValue += 5 
	# 		for i in xrange(0,xIteration*2):
	# 			xValue -= 5
	# 			self._ik.bodyFK(xValue,0,0,0,0,0)
	# 			time.sleep(0.05)
	# 		for i in xrange(0,xIteration):
	# 			xValue += 5
	# 			self._ik.bodyFK(xValue,0,0,0,0,0)
	# 			time.sleep(0.05)			

	def bodyFKY(self, times, maxY):
		yIteration = maxY/5
		yValue = 0
		for y in xrange(0,times):
			for i in xrange(0,yIteration):
				if y > 0:
					yValue += 5
				self._ik.bodyFK(0,yValue,0,0,0,0)
				time.sleep(0.05)
				if y == 0:
					yValue += 5 
			for i in xrange(0,yIteration*2):
				yValue -= 5
				self._ik.bodyFK(0,yValue,0,0,0,0)
				time.sleep(0.05)
			for i in xrange(0,yIteration):
				yValue += 5
				self._ik.bodyFK(0,yValue,0,0,0,0)
				time.sleep(0.05)

	def bodyFKZ(self, times, maxZ):
		zIteration = maxZ/5
		zValue = 0
		for z in xrange(0,times):
			for i in xrange(0,zIteration):
				if z > 0:
					zValue += 5
				self._ik.bodyFK(0,0,zValue,0,0,0)
				time.sleep(0.05)
				if z == 0:
					zValue += 5 
			for i in xrange(0,zIteration*2):
				zValue -= 5
				self._ik.bodyFK(0,0,zValue,0,0,0)
				time.sleep(0.05)
			for i in xrange(0,zIteration):
				zValue += 5
				self._ik.bodyFK(0,0,zValue,0,0,0)
				time.sleep(0.05)


	def Dance(self):
		#self.bodyFKX(3,25)
		self.bodyFKY(3,20)#Max 20

		# for x in xrange(1,5):
		# 	self._ik.bodyFK(0, 5, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 10, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 15, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 20, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 25, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 20, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 15, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 10, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 5, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 0, 0, 0, 0, 0)

		# 	self._ik.bodyFK(0, -5, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, -10, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, -15, 0, 0, 0, 0)
		# 	time.sleep(0.05)			
		# 	self._ik.bodyFK(0, -20, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, -25, 0, 0, 0, 0)
		# 	time.sleep(0.05)


		# for x in xrange(1,5):
		# 	self._ik.bodyFK(5, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(10, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(15, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(20, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(25, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(20, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(15, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(10, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(5, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 0, 0, 0, 0, 0)

		# 	self._ik.bodyFK(-5, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-10, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-15, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-20, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-25, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-20, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-15, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-10, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(-5, 0, 0, 0, 0, 0)
		# 	time.sleep(0.05)
		# 	self._ik.bodyFK(0, 0, 0, 0, 0, 0)

		self._Walk = True


dnce = Dance()
dnce.Dance()
