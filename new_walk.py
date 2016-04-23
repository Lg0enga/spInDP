import time
from ax12 import Ax12
ax12 = Ax12()

__author__ = 'Jelmer Visser'

speed = 1

firstServoMove = None
secondServoMove = None
thirdServoMove = None


def resetMoves():
    firstServoMove = None
    secondServoMove = None
    thirdServoMove = None


def waitForServos():
    while firstServoMove is None and secondServoMove is None and thirdServoMove is None:
        time.sleep(0.00005)
    resetMoves()


def walk():
    while True:
        firstServoMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 355, int(245 * speed))
        thirdServoMove = ax12.moveSpeed(12, 110, int(511 * speed))
        waitForServos()
        firstServoMove = ax12.moveSpeed(10, 665, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 428, int(245 * speed))
        thirdServoMove = ax12.moveSpeed(12, 263, int(511 * speed))
        waitForServos()
        secondServoMove = ax12.moveSpeed(11, 467, int(512 * speed))
        thirdServoMove = ax12.moveSpeed(12, 291, int(371 * speed))
        waitForServos()
        firstServoMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 404, int(209 * speed))
        thirdServoMove = ax12.moveSpeed(12, 138, int(509 * speed))
        waitForServos()
        firstServoMove = ax12.moveSpeed(10, 358, int(512 * speed))
        secondServoMove = ax12.moveSpeed(11, 467, int(209 * speed))
        thirdServoMove = ax12.moveSpeed(12, 291, int(509 * speed))
        waitForServos()
        secondServoMove = ax12.moveSpeed(11, 428, int(512 * speed))
        thirdServoMove = ax12.moveSpeed(12, 263, int(371 * speed))


def main():
    walk()

if __name__ == '__main__':
    main()
