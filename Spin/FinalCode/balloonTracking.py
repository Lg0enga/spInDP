# USAGE python object_movement.py --video
# object_tracking_example.mp4 python object_movement.py
# import the necessary packages yo
from collections import deque
import numpy as np
import argparse
import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import math
import sys
from threading import Thread

sys.path.insert(0, '/home/pi/spInDP/Spin/Loopscripts')

from walk_test import Walk
walk = Walk()

from classes.ik import IK

class Vision(object):

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-c", "--color", type=str, default="", help="object color")
	ap.add_argument("-b", "--buffer", type=int, default=8, help="max buffer size")
	args = vars(ap.parse_args())
	# define the lower and upper boundaries of the "threshold"
	# in the HSV color space
	if args["color"] == "lokaal":
		blueDict = {
	    'lowerColor' : (42,142,135),
	    'upperColor' : (121,255,243)
		}
		redDict = {
	    'lowerColor' : (151,130,132),
	    'upperColor' : (187,255,255)
		}
	if args["color"] == "kuil":
		blueDict = {
	    'lowerColor' : (87,0,55),
	    'upperColor' : (131,255,255)
		}
		redDict = {
	    'lowerColor' : (0,187,143),
	    'upperColor' : (11,255,255)
		}
	else:		#Default
		blueDict = {
	    'lowerColor' : (42,142,135),
	    'upperColor' : (121,255,243)
		}
		redDict = {
	    'lowerColor' : (151,130,132),
	    'upperColor' : (187,255,255)
		}
	# initialize the list of tracked points, the frame counter,
	# and the coordinate deltas
	pts = deque(maxlen=args["buffer"])
	counter = 0

	direction = ""
	prikDelayCounter = 0
	#initialize the pi Camera and set its settings
	camera = PiCamera()
	camera.resolution = (640, 480)
	camera.framerate = 32
	camera.awb_mode = "auto"
	camera.meter_mode = "matrix"
	#make an PiRGBArray which get filled with the frames captured
	rawCapture = PiRGBArray(camera, size=(640,480))
	#give 1 second for the pi to set itself correctly
	time.sleep(1)

	def __init__(self):
		self.previousTime = 0
		self._ik = IK()
		self._ik.initInitialPositions()
		print "test"
	#Function for the puncture motion
	def punctureBalloon():
		walk.Prik()
	#function for calculation the distance to object
	#x: area of object in pixels
	def calculateDistance(self, x):
			return math.ceil(-22.38 * math.log1p(x) + 293.25)
	#function for determining the spiders walking direction
	#x: X-coordinate of the vision object
	def spiderDirection(self, x):
		print "test"
		while True:
			currentTime = int(round(time.time() * 1000))
			if currentTime - self.previousTime >= self._ik._servoUpdatePeriod:
				self.previousTime = currentTime
				#if the value of x is smaller than 270 it is considered left of center
				if x < 270:
					self._ik.initTripod(0,-512,0)
					self._ik.bodyFK(0, 0, 0, 0, 0, 0)
					cv2.putText(self.frame, "Left!",
					(550, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
				#if the value of x is greater than 370 it is considered right of center
				elif x > 370:
					self._ik.initTripod(0,512,0)
					self._ik.bodyFK(0, 0, 0, 0, 0, 0)
					cv2.putText(self.frame, "Right!",
					(550, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
				#if the value of x is between the other 2 values it is considered in center
				else:
					self._ik.initTripod(512,0,0)
					self._ik.bodyFK(0, 0, 0, 0, 0, 0)
					cv2.putText(self.frame, "Forward!",
					(550, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
	#function to display the distance of the objects center to the distance of the camera center
	#color: the balloon color(s) found in the frame
	def displayDistanceToCenter(self, color):
		(x, y) = (0, 0)
		#display either the red or blue distance
		if color == "red":
			cv2.putText(self.frame, "Rood x: {}, y: {}".format(round(abs(x-self.centerX),2), round(abs(y-self.centerY),2)),
			(10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
		elif color == "blue":
			cv2.putText(self.frame, "Blauw x: {}, y: {}".format(round(abs(x-self.centerX),2), round(abs(y-self.centerY),2)),
			(10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)
		elif color == "both":
			cv2.putText(self.frame, "Rood x: {}, y: {}".format(round(abs(x-self.centerX),2), round(abs(y-self.centerY),2)),
			(10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			cv2.putText(self.frame, "Blauw x: {}, y: {}".format(round(abs(x2-self.centerX),2), round(abs(y2-self.centerY),2)),
			(10, self.frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)

	def displayScreen(self):
		#the main loop for displaying and running vision on the camara stream
		for stream in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
			# grab the raw NumPy array representing the image
			self.frame = stream.array
			#frame = imutils.resize(image, width=640)
			hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

			# construct a mask for the color, then perform
			# a series of dilations and erosions to remove any small
			# blobs left in the mask
			mask1 = cv2.inRange(hsv, self.redDict["lowerColor"], self.redDict["upperColor"])
			mask1 = cv2.erode(mask1, None, iterations=2)
			mask1 = cv2.dilate(mask1, None, iterations=2)

			mask2 = cv2.inRange(hsv, self.blueDict["lowerColor"], self.blueDict["upperColor"])
			mask2 = cv2.erode(mask2, None, iterations=2)
			mask2 = cv2.dilate(mask2, None, iterations=2)

			# find contours in the mask and initialize the current
			# (x, y) center of the ball
			cnts = cv2.findContours(mask1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
			cnts2 = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
			center = None
			imageCenter = (320, 240)
			self.centerX = 320
			self.centerY = 240

			#If a red contour and a blue contour are both found then the code runs this codeblock
			if len(cnts and cnts2) > 0:
				# find the largest contour in the mask, then use
				# it to compute the minimum enclosing circle and
				# centroid
				c = max(cnts, key=cv2.contourArea)								#the largest contour
				((x, y), radius) = cv2.minEnclosingCircle(c) 					#minimum enclosing circle
				M = cv2.moments(c)												#information about the contour
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 	#the center of the contour

				#the same for the blue contour
				c2 = max(cnts2, key=cv2.contourArea)

				self.x2 = 0
				self.y2 = 0

				((x2, y2), radius2) = cv2.minEnclosingCircle(c2)
				M2 = cv2.moments(c2)
				center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))

				# only proceed if the radius meets a minimum size
				# in this case if both the blue and red contour are big enough
				if radius > 20 and radius2 > 20:
					# draw the circle and centroid on the frame,
					cv2.circle(self.frame, (int(x), int(y)), int(radius),(0, 0, 255), 2)
					cv2.circle(self.frame, (int(x2), int(y2)), int(radius2),(255, 0, 0), 2)
					cv2.circle(self.frame, center, 5, (0, 255, 0), -1)
					cv2.circle(self.frame, center2, 5, (0, 255, 0), -1)
					#lines between the center of the screen and the center of the objects
					cv2.line(self.frame, center, imageCenter, (0, 0, 255), 2)
					cv2.line(self.frame, center2, imageCenter, (255, 0, 0), 2)

					#call to the function for distance to center calculation on both balloons
					self.displayDistanceToCenter("both")

					#call the the function for distance calculation from camera to object
					objectDistance = self.calculateDistance(M["m00"])
					cv2.putText(self.frame, "Afstand: {} cm".format(self.calculateDistance(M["m00"])),(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)

					#call to the spiderwalking function
					#x: x-coordinate of object
					spiderDirection(x)

					#pts.appendleft(center)
					#pts.appendleft(center2)

				#if only the red contour is big enough this code block runs
				elif radius > 20:
					# draw the circle and centroid on the frame,
					cv2.circle(self.frame, (int(x), int(y)), int(radius),(0, 0, 255), 2)
					cv2.circle(self.frame, center, 5, (0, 255, 0), -1)
					cv2.line(self.frame, center, imageCenter, (0, 0, 255), 2)

					#call to the function for distance to center calculation on the red balloon
					self.displayDistanceToCenter("red")

					#call the the function for distance calculation from camera to object
					objectDistance = self.calculateDistance(M["m00"])
					cv2.putText(self.frame, "Afstand: {} cm".format(self.calculateDistance(M["m00"])),(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)

					#call to the spiderwalking function
					#x: x-coordinate of object
					self.spiderDirection(x)
					#pts.appendleft(center)

				#if only the blue contour is big enough this code block runs
				elif radius2 > 20:
					# draw the circle and centroid on the frame,
					cv2.circle(self.frame, (int(x2), int(y2)), int(radius2),
						(255, 0, 0), 2)
					cv2.circle(self.frame, center2, 5, (0, 255, 0), -1)
					cv2.line(self.frame, center2, imageCenter, (255, 0, 0), 2)

					#call to the function for distance to center calculation on the blue balloon
					self.displayDistanceToCenter("blue")

			#if only a red contour is found this code block runs
			elif len(cnts) > 0:
				# find the largest contour in the mask, then use
				# it to compute the minimum enclosing circle and
				# centroid
				c = max(cnts, key=cv2.contourArea)								#the largest contour
				((x, y), radius) = cv2.minEnclosingCircle(c)					#minimum enclosing circle
				M = cv2.moments(c)												#information about the contour
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))	#the center of the contour

				# if the red contour is big enough this code block runs
				if radius > 20:

					# draw the circle and centroid on the frame,
					cv2.circle(self.frame, (int(x), int(y)), int(radius),(0, 0, 255), 2)
					cv2.circle(self.frame, center, 5, (0, 255, 0), -1)
					cv2.line(self.frame, center, imageCenter, (0, 0, 255), 2)

					#call to the function for distance to center calculation on the red balloon
					self.displayDistanceToCenter("red")
					cv2.putText(self.frame, "Afstand: {} cm".format(self.calculateDistance(M["m00"])),(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)

					#if the distance from camera to the red balloon is smaller than 18cm it performs this block
					#this is to prevent the prik function to be called more than once in less than 10 frames
					if self.calculateDistance(M["m00"]) < 18.0:
						if prikDelayCounter == 0:				#test to see of the counter is 0
							prikDelayCounter = self.counter			#set the counter to the number of the frame in which the balloon is at 18cm
							punctureBalloon()					#run the puncture function
						elif (prikDelayCounter+10) < self.counter:	#if the prikDelayCounter+10 is smaller than the current frame number
							prikDelayCounter = 0				#reset the prikDelayCounter

					#call to the spiderwalking function
					#x: x-coordinate of object
					self.spiderDirection(x)
			elif len(cnts2) > 0:
				# find the largest contour in the mask, then use
				# it to compute the minimum enclosing circle and
				# centroid
				c = max(cnts2, key=cv2.contourArea)
				((x, y), radius) = cv2.minEnclosingCircle(c)
				M = cv2.moments(c)
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

				# only proceed if the radius meets a minimum size
				if radius > 20:
					# draw the circle and centroid on the frame,
					# then update the list of tracked points
					cv2.circle(self.frame, (int(x), int(y)), int(radius),
						(255, 0, 0), 2)
					cv2.circle(self.frame, center, 5, (0, 255, 0), -1)
					cv2.line(self.frame, center, imageCenter, (255, 0, 0), 2)

					#call to the function for distance to center calculation on the blue balloon
					self.displayDistanceToCenter("blue")

			#show the frame to our screen and increment the frame counter
			#cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF
			self.counter += 1
			self.rawCapture.truncate(0)	#empty the frame for the next one

			# if the 'q' key is pressed, stop the loop
			if key == ord("q"):
				break

		# cleanup the self.camera. and close any open windows
		self.camera.release()
		cv2.destroyAllWindows()

vision = Vision()
vision.displayScreen()
