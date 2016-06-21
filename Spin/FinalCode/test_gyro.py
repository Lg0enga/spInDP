from classes.gyro_MPU import GyroData
import time

GD = GyroData()
i = 0
while True:
    print "X" + str(GD.getGyroDataX(i))
    print "Y" + str(GD.getGyroDataY(i))
    time.sleep(1)
    i+=1
