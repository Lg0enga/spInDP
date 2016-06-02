from classes.ik import IK
import time

ik = IK()
ik.initInitialPositions()

test = 0
back = False

while True:
    millis = int(round(time.time() * 1000))
    currentTime = millis
    previousTime = 0

    if (currentTime - previousTime >= ik._servoUpdatePeriod):
        previousTime = currentTime

        ik.initTripod(0, 0, 0)

        # if test == 0:
        #     back = True
        #
        # if test == -100:
        #     back = False
        #
        # if back:
        #     test -= 1
        # else:
        #     test += 1

        ik.bodyFK(0, 0, 0, 50, 0, 0)
        ik.legIK()
        ik.driveServos()
    else:
        time.sleep(0.01)
