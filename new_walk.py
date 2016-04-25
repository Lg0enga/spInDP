import time
import array
from ax12 import Ax12
ax12 = Ax12()

__author__ = 'Jelmer Visser'

speed = 2

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

        time.sleep(0.01)


def degreesToBits(degrees):
    return int((1023 * degrees) / 300)


def walk():
    while True:
        firstServoMove = ax12.moveSpeed(10, degreesToBits(150), int(1023 * speed))
        secondServoMove = ax12.moveSpeed(11, degreesToBits(104), int(491 * speed))
        thirdServoMove = ax12.moveSpeed(12, degreesToBits(32.2), int(1021 * speed))
        time.sleep(0.20)
        firstServoMove = ax12.moveSpeed(10, degreesToBits(195), int(1023 * speed))
        secondServoMove = ax12.moveSpeed(11, degreesToBits(125.6), int(491 * speed))
        thirdServoMove = ax12.moveSpeed(12, degreesToBits(77.1), int(1021 * speed))
        time.sleep(0.20)
        secondServoMove = ax12.moveSpeed(11, degreesToBits(137), int(1023 * speed))
        time.sleep(0.1)
        firstServoMove = ax12.moveSpeed(10, degreesToBits(150), int(1023 * speed))
        secondServoMove = ax12.moveSpeed(11, degreesToBits(118.6), int(417 * speed))
        thirdServoMove = ax12.moveSpeed(12, degreesToBits(40.6), int(1018 * speed))
        time.sleep(0.20)
        firstServoMove = ax12.moveSpeed(10, degreesToBits(105), int(1023 * speed))
        secondServoMove = ax12.moveSpeed(11, degreesToBits(137), int(417 * speed))
        thirdServoMove = ax12.moveSpeed(12, degreesToBits(85.4), int(1018 * speed))
        time.sleep(0.20)
        secondServoMove = ax12.moveSpeed(11, degreesToBits(125.6), int(1023 * speed))
        thirdServoMove = ax12.moveSpeed(12, degreesToBits(77.1), int(741 * speed))
        time.sleep(0.1)

def main():
    walk()

if __name__ == '__main__':
    main()
