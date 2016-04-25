import time
from ax12 import Ax12
ax12 = Ax12()

__author__ = 'Jelmer Visser'

speed = 1

moving = False

def wait_stopped(self, ids=None):
    """
    Wait for a specific motor or all motors on the chain to have stopped moving.
    This is a blocking function.
    """
    while True:
        moving = False
        for id in ids:
            if ax12.readPosition(id) != 0:
                moving = True
                break
        if not moving:
            break
        time.sleep(0.1)

def walk():
    while True:
        firstServoMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 355, int(245 * speed))
        thirdServoMove = ax12.moveSpeed(12, 110, int(511 * speed))
        wait_stopped({10, 11, 12})
        firstServoMove = ax12.moveSpeed(10, 665, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 428, int(245 * speed))
        thirdServoMove = ax12.moveSpeed(12, 263, int(511 * speed))
        wait_stopped({10, 11, 12})
        secondServoMove = ax12.moveSpeed(11, 467, int(512 * speed))
        thirdServoMove = ax12.moveSpeed(12, 291, int(371 * speed))
        wait_stopped({11, 12})
        firstServoMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 404, int(209 * speed))
        thirdServoMove = ax12.moveSpeed(12, 138, int(509 * speed))
        wait_stopped({10, 11, 12})
        firstServoMove = ax12.moveSpeed(10, 358, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 467, int(209 * speed))
        thirdServoMove = ax12.moveSpeed(12, 291, int(509 * speed))
        wait_stopped({10, 11, 12})
        secondServoMove = ax12.moveSpeed(11, 428, int(512 * speed))
        thirdServoMove = ax12.moveSpeed(12, 263, int(371 * speed))
        wait_stopped({11, 12})

def main():
    walk()

if __name__ == '__main__':
    main()
