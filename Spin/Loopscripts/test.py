import time
import threading
import pygame
from threading import Thread
from ax12 import Ax12
ax12 = Ax12()

from walk_test import Walk
walk = Walk()

#print walk.findServos()

#print ax12.setID(1, 10)

# walk.setTorque(512)

#walk.readTemperature()
#walk.oldBeginPosition()

#walk.doFactoryReset()

#walk.setReturnDelayTime()
# walk.getReturnDelayTime()

walk.Prik()
#time.sleep(5)
#Thread(target = walk.driveToWalk).start()

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
