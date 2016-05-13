import time
import threading
import pygame
from threading import Thread
from ax12 import Ax12
ax12 = Ax12()

from new_walk import Walk
walk = Walk()

pygame.joystick.init()

while True:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
#print walk.findServos()

#ax12.setID(1, 62)

#walk.oldBeginPosition()

# walk.setReturnDelayTime()
# walk.getReturnDelayTime()

# while True:
#     try:
#         walk.beginPosition()
#     except ax12.timeoutError:
#         print "timeout"

#walk.set_speed(0.3)
# Thread(target = walk.beginPosition).start()
# time.sleep(1)
# walk.set_speed(0.6)
# time.sleep(1)
# walk.set_speed(0.7)
# time.sleep(1)
# walk.set_speed(0.8)
# time.sleep(1)
# walk.set_speed(0.9)
# time.sleep(1)
# walk.set_speed(1)
# time.sleep(1)
# walk.stop()
