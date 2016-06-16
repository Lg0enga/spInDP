from classes.gyro_MPU import GyroData
import time

GD = GyroData()
i = 0
while True:
    GD.getGyroDataX(i)
    GD.getGyroDataY(i)
    time.sleep(1)
    i+=1
