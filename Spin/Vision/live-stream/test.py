import cv2 as cv
import picamera
import socket
import time

socket = socket.socket()
socket.bind(('', 9000))
socket.listen(0)

cam = picamera.PiCamera()
cam.resolution = (640,480)
cam.framerate = 28

conn = socket.accept()
print conn

#for stream in cam.capture_continuous(raw, format="bgr", use_video_port=True):
# while True:
# 	#img = stream.array
# 	# img = cam.capture(conn, format="bgr")

# 	cam.start_recording(conn, format='h264')
# 	cam.wait_recording(300)
# 	cam.stop_recording()

# 	if cv.WaitKey(10) == 27:
# 		break