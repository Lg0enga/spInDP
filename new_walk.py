import time
import array
import math
from ax12 import Ax12
ax12 = Ax12()

__author__ = 'Jelmer Visser'

speed = 2
x = 150
y = 150
z = 60
z1 = 20
CL = 53
FL = 83
TL = 126

moving = False

def wait_stopped():
    """
    Wait for a specific motor or all motors on the chain to have stopped moving.
    This is a blocking function.
    """
    moving = True

    while moving:
        try:
            if ax12.readMovingStatus(10) == 0 and ax12.readMovingStatus(11) == 0 and ax12.readMovingStatus(12) == 0:
                moving = False
                break
        except Exception:
            moving = True


def degreesToBits(degrees):
    return int((1023 * degrees) / 300)


def walk():
    while True:
        firstServoMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 355, int(245 * speed))
        thirdServoMove = ax12.moveSpeed(12, 110, int(511 * speed))
        time.sleep(0.25)
        firstServoMove = ax12.moveSpeed(10, 665, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 428, int(245 * speed))
        thirdServoMove = ax12.moveSpeed(12, 263, int(511 * speed))
        time.sleep(0.25)
        secondServoMove = ax12.moveSpeed(11, 467, int(512 * speed))
        thirdServoMove = ax12.moveSpeed(12, 291, int(371 * speed))
        time.sleep(0.14)
        firstServoMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 404, int(209 * speed))
        thirdServoMove = ax12.moveSpeed(12, 138, int(509 * speed))
        time.sleep(0.25)
        firstServoMove = ax12.moveSpeed(10, 358, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 467, int(209 * speed))
        thirdServoMove = ax12.moveSpeed(12, 291, int(509 * speed))
        time.sleep(0.25)
        secondServoMove = ax12.moveSpeed(11, 428, int(512 * speed))
        thirdServoMove = ax12.moveSpeed(12, 263, int(371 * speed))
        time.sleep(0.14)

def main():
    walk()

if __name__ == '__main__':
    main()
