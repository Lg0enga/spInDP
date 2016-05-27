import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.annotate_text = ''
 
    # camera.image_effect = 'gpen'
    # Give the camera some time to adjust to conditions    
    print 'Type "stop" to abort'
    while bool:
	time.sleep(1)
 	key = raw_input()
	if key == "stop":
            bool = False
