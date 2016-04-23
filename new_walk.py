__author__ = 'Jelmer Visser'

from ax12 import Ax12
import time

speed = 1

firstServoMove = None
secondServoMove = None
thirdServoMove = None

def resetMoves():
    firstServoMove = None
    secondServoMove = None
    thirdServoMove = None

def waitForServos():
    while firstServoFirstMove == None and secondServoFirstMove == None and thirdServoFirstMove == None:
        time.sleep(0.00005)
    resetMoves()

def walk():
    while True:
        firstServoFirstMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoFirstMove = ax12.moveSpeed(11, 355, int(245 * speed))
        thirdServoFirstMove = ax12.moveSpeed(12, 110, int(511 * speed))

        waitForServos()

        firstServoFirstMove = ax12.moveSpeed(10, 665, int(512 * speed))
        secondServoFirstMove = ax12.moveSpeed(11, 428, int(245 * speed))
        thirdServoFirstMove = ax12.moveSpeed(12, 263, int(511 * speed))

        waitForServos()

        secondServoFirstMove = ax12.moveSpeed(11, 467, int(512 * speed))
        thirdServoFirstMove = ax12.moveSpeed(12, 291, int(371 * speed))

        waitForServos()

        firstServoFirstMove = ax12.moveSpeed(10, 512, int(512 * speed))
        secondServoFirstMove = ax12.moveSpeed(11, 404, int(209 * speed))
        thirdServoFirstMove = ax12.moveSpeed(12, 138, int(509 * speed))

        waitForServos()

        firstServoFirstMove = ax12.moveSpeed(10, 358, int(512 * speed))
        secondServoFirstMove = ax12.moveSpeed(11, 467, int(209 * speed))
        thirdServoFirstMove = ax12.moveSpeed(12, 291, int(509 * speed))

        waitForServos()

        secondServoFirstMove = ax12.moveSpeed(11, 428, int(512 * speed))
        thirdServoFirstMove = ax12.moveSpeed(12, 263, int(371 * speed))

def main():
    walk()

if __name__ == '__main__':
    main()
