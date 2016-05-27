import picamera
import time

camera = picamera.PiCamera()

camera.video_stabilization = True
#camera.brightness = 75

camera.start_preview()
time.sleep(1001)
