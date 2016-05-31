import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.annotate_text = ''
 
    # camera.image_effect = 'gpen'
    # Give the camera some time to adjust to conditions
    bool = True    
    count = 10    
    while count != 0:
	camera.annotate_text = str(count)	
	time.sleep(1)
	count-=1
