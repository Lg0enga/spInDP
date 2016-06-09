from livestream.stream import LiveStream
from picamera.array import PiRGBArray
from collections import deque 
from picamera import PiCamera
import numpy as np 
import subprocess
import imutils 
import time
import sys
import cv2 

# Color value of white stripe
# 90 45 58 255 89 255

# set up pi camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

# stream = LiveStream(camera)
# stream.start()

#set up parameters for furyroad
lower = np.array([0, 0, 106])
upper = np.array([130, 57, 255])

# stop the livestream 
# subprocess.call("/home/pi/RPi_Cam_Web_Interface/stop.sh")

counter = 0

# warm up camera
time.sleep(2)

for stream in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	print "in ze loop"
	try: 
		frame = stream.array
		crop = frame[10:300,70:570]
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		hsvCrop = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
		

		thresh = cv2.inRange(hsv, lower, upper)
		thresh = cv2.erode(thresh, None, iterations=5)
		thresh = cv2.dilate(thresh, None, iterations=8)	
		threshCrop = cv2.inRange(hsvCrop, lower, upper)
		threshCrop = cv2.erode(threshCrop, None, iterations=5)
		threshCrop = cv2.dilate(threshCrop, None, iterations=8)

		#main rectangle
		cv2.rectangle(frame, (70,10), (570,300), (255,0,0), 2)
		#left sector
		cv2.rectangle(frame, (70,10), (140,300), (255,0,0), 2)
		#right sector
		cv2.rectangle(frame, (500,10), (570,300), (255,0,0), 2)

		cropContours, hierarchy = cv2.findContours(threshCrop.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		if len(cropContours) > 0:
			cropContours = cropContours[0] if imutils.is_cv2() else cropContours[1]	
			# Determine the most extreme points along the contour
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
			
			# if the worth of extLeft is below 70, it means shape contour is on the left side of the rectangle.
			# Same goes for right, if both cases is false, the spider needs to go straight ahead			
			if extLeft[0] < 70:		
				cv2.putText(frame, "Turn Left!!!",
					(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			elif extRight[0] > 430:
				cv2.putText(frame, "Turn Right!!!",
					(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			else:
				cv2.putText(frame, "Straight Ahead!!!",
					(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)    	
	   	
		cv2.imshow("thresh", thresh)
		cv2.imshow("threshCrop", threshCrop)
		cv2.imshow("frame", frame)
		cv2.imshow("crop", crop)

		key = cv2.waitKey(1) & 0xFF
		counter += 1
		rawCapture.truncate(0)
		if key == ord("q"):
			break
	except:
		print sys.exc_info()
		sys.exit()

camera.release()
cv2.destroyAllWindows()	