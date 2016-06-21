from picamera.array import PiRGBArray
from collections import deque
from picamera import PiCamera
import numpy as np
import imutils
import time
import cv2
import subprocess
import threading
import sys
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

sys.path.insert(0, '/home/pi/spInDP/Spin/Loopscripts')

from walk_test import Walk
walk = Walk()

from classes.ik import IK

class FuryRoad(object):

	def __init__(self):
		pwm.set_pwm(9, 0, 4095)

		self._previousTime = 0
		self._x = 0
        	self._y = 0
        	self._r = 0
		self._Walk = False

		self._WalkTest = threading.Thread(target=self.WalkTest)
		self._WalkTest.start()

		self._ik = IK()
		self._ik.initInitialPositions()
		self._contourCheck = 0

	def WalkTest(self):
		while True:
			while self._Walk:
				currentTime = int(round(time.time() * 1000))

				if currentTime - self._previousTime >= self._ik._servoUpdatePeriod:
					self._previousTime = currentTime
					self._ik.initRipple(self._x, self._y, self._r)
					self._ik.bodyFK(0, 0, 0, 0, 0, 0)

	def spiderDirection(self, extLeft, extRight, extTop):
		if extLeft < 70:
			self._x = 250
			self._y = 0
			self._r = 220
			self._Walk = True
		elif extRight > 430:
			self._x = 250
			self._y = 0
			self._r = -220
			self._Walk = True
		# elif extTop > 380:
			# self._x = 0
			# self._y = 0
			# self._r = 0
			# self._Walk = False
		else:
			self._x = 512
			self._y = 0
			self._r = 0
			self._Walk = True

	def detectFuryroad(self):
		self.camera = PiCamera()
		self.camera.resolution = (640, 480)
		self.camera.framerate = 15
		self.rawCapture = PiRGBArray(self.camera, size=(640,480))

		self.lower = np.array([46, 0, 112])
		self.upper = np.array([255, 255, 255])

		self.counter = 0

		time.sleep(2)

		for stream in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
			frame = stream.array
			crop = frame[200:300,5:635]
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			hsvCrop = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)

			thresh = cv2.inRange(hsv, self.lower, self.upper)
			thresh = cv2.erode(thresh, None, iterations=5)
			thresh = cv2.dilate(thresh, None, iterations=8)
			threshCrop = cv2.inRange(hsvCrop,self. lower, self.upper)
			threshCrop = cv2.erode(threshCrop, None, iterations=5)
			threshCrop = cv2.dilate(threshCrop, None, iterations=8)

			#main rectangle
			cv2.rectangle(frame, (5,200), (635,300), (255,0,0), 2)
			#left sector
			cv2.rectangle(frame, (5,200), (80,300), (255,0,0), 2)
			#right sector
			cv2.rectangle(frame, (560,200), (635,300), (255,0,0), 2)

			im2, cropContours, hierarchy = cv2.findContours(threshCrop.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
			if len(cropContours) > 0:
				cropContours = cropContours[0]
				# M = cv2.moments(cropContours)
				# print M['m00']
				# determine the most extreme points along the contour
				extLeft = tuple(cropContours[cropContours[:, :, 0].argmin()][0])
				extRight = tuple(cropContours[cropContours[:, :, 0].argmax()][0])
				extTop = tuple(cropContours[cropContours[:, :, 1].argmin()][0])
				extBot = tuple(cropContours[cropContours[:, :, 1].argmax()][0])

				#draw the extreme points
				cv2.drawContours(crop, [cropContours], -1,(0,255,0), 3)
				cv2.circle(crop, extLeft, 8, (0, 0, 255), -1)
				cv2.circle(crop, extRight, 8, (0, 255, 0), -1)
				cv2.circle(crop, extTop, 8, (255, 0, 0), -1)
				cv2.circle(crop, extBot, 8, (255, 255, 0), -1)
				self.spiderDirection(extLeft[0], extRight[0], extTop[0])
			#cv2.imshow("thresh", thresh)
			# cv2.imshow("threshCrop", threshCrop)
			#cv2.imshow("frame", frame)
			# cv2.imshow("crop", crop)

			key = cv2.waitKey(1) & 0xFF
			self.counter += 1
			self.rawCapture.truncate(0)
			if key == ord("q"):
				break

		self.camera.release()
		cv2.destroyAllWindows()

furyroad = FuryRoad()
furyroad.detectFuryroad()
