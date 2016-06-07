from picamera import PiCamera
from stream import LiveStream

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

# stream = LiveStream((640,480), 28, PiCamera())
stream = LiveStream(camera)

if stream.start():
	print "Connecting to server.."
	
	while stream.streaming():
		pass
