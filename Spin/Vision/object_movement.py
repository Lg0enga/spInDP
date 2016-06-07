from livestream.stream import LiveStream
from picamera.array import PiRGBArray
from collections import deque 
from picamera import PiCamera
import numpy as np 
import argparse 
import imutils 
import thread
import time
import math
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser() 
ap.add_argument("-c", "--color", type=str, default="", help="object color") 
ap.add_argument("-b", "--buffer", type=int, default=8, help="max buffer size") 
args = vars(ap.parse_args())

# define the lower and upper boundaries of the balloons depending on the area
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
else:
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
(x, y) = (0, 0) 
direction = "" 

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

socketStream = LiveStream(camera)
socketStream.start()

camera.awb_mode = "auto"
camera.meter_mode = "matrix"

time.sleep(0.1)

def calculateDistance(x):	
	return math.ceil(-22.38 * math.log1p(x) + 293.25)

for stream in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):	
	# grab the raw NumPy array representing the image
	frame = stream.array
	#frame = imutils.resize(image, width=640)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# construct a mask for the color, then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	#mask1 = cv2.inRange(hsv, lowerColor, upperColor)

	mask1 = cv2.inRange(hsv, redDict["lowerColor"], redDict["upperColor"])
	mask1 = cv2.erode(mask1, None, iterations=2)
	mask1 = cv2.dilate(mask1, None, iterations=2)
	
	mask2 = cv2.inRange(hsv, blueDict["lowerColor"], blueDict["upperColor"])
	mask2 = cv2.erode(mask2, None, iterations=2)
	mask2 = cv2.dilate(mask2, None, iterations=2)
	
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	cnts2 = cv2.findContours(mask2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	imageCenter = (320, 240)
	centerX = 320
	centerY = 240

	camera.start_recording(socketStream.conn, format='h264')
	camera.wait_recording(1)
	camera.stop_recording()
	
	if len(cnts and cnts2) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))		
		
		c2 = max(cnts2, key=cv2.contourArea)
		((x2, y2), radius2) = cv2.minEnclosingCircle(c2)
		M2 = cv2.moments(c2)
		center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))
 
		# only proceed if the radius meets a minimum size
		if radius > 20 and radius2 > 20:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 0, 255), 2)
			cv2.circle(frame, (int(x2), int(y2)), int(radius2),
				(255, 0, 0), 2)
			cv2.circle(frame, center, 5, (0, 255, 0), -1)
			cv2.circle(frame, center2, 5, (0, 255, 0), -1)
			cv2.line(frame, center, imageCenter, (0, 0, 255), 2)
			cv2.line(frame, center2, imageCenter, (255, 0, 0), 2)
			
			cv2.putText(frame, "Rood x: {}, y: {}".format(round(abs(x-centerX),2), round(abs(y-centerY),2)),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			cv2.putText(frame, "Blauw x: {}, y: {}".format(round(abs(x2-centerX),2), round(abs(y2-centerY),2)),
			(10, frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)
			
			cv2.putText(frame, "Afstand: {} cm".format(calculateDistance(M["m00"])),
			(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			cv2.putText(frame, "Afstand: {} cm".format(calculateDistance(M2["m00"])),
			(10, 40), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)

			#pts.appendleft(center)	
			#pts.appendleft(center2)
		elif radius > 20:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 0, 255), 2)
			cv2.circle(frame, center, 5, (0, 255, 0), -1)
			cv2.line(frame, center, imageCenter, (0, 0, 255), 2)
			cv2.putText(frame, "Rood x: {}, y: {}".format(round(abs(x-centerX),2), round(abs(y-centerY),2)),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)

			cv2.putText(frame, "Afstand: {} cm".format(calculateDistance(M["m00"])),
			(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			
			#pts.appendleft(center)
		elif radius2 > 20:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x2), int(y2)), int(radius2),
				(255, 0, 0), 2)
			cv2.circle(frame, center2, 5, (0, 255, 0), -1)
			cv2.line(frame, center2, imageCenter, (255, 0, 0), 2)
			cv2.putText(frame, "Rood x: {}, y: {}".format(round(abs(x-centerX),2), round(abs(y-centerY),2)),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)
			#pts.appendleft(center2)
			cv2.putText(frame, "Afstand: {} cm".format(calculateDistance(M["m00"])),
			(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)

	elif len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 20:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 0, 255), 2)
			cv2.circle(frame, center, 5, (0, 255, 0), -1)
			cv2.line(frame, center, imageCenter, (0, 0, 255), 2)
			cv2.putText(frame, "Rood x: {}, y: {}".format(round(abs(x-centerX),2), round(abs(y-centerY),2)),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			#pts.appendleft(center)
			
			# y = -0.1x+70 
			cv2.putText(frame, "Afstand: {} cm".format(calculateDistance(M["m00"])),
			(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 255), 2)
			
 
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
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(255, 0, 0), 2)
			cv2.circle(frame, center, 5, (0, 255, 0), -1)
			cv2.line(frame, center, imageCenter, (255, 0, 0), 2)
			cv2.putText(frame, "Rood x: {}, y: {}".format(round(abs(x-centerX),2), round(abs(y-centerY),2)),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)
			#pts.appendleft(center)	
			
			# y = -0.1x+70 
			cv2.putText(frame, "Afstand: {} cm".format(calculateDistance(M["m00"])),
			(10, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)
 
	# show the frame to our screen and increment the frame counter
	# cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	counter += 1
	rawCapture.truncate(0)
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()	
	
