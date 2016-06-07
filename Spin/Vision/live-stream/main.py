from picamera import camera
from stream import LiveStream

stream = LiveStream((640,480), 28)

if stream.start():
	print "Connecting to server.."
	
	while stream.streaming():
		pass
