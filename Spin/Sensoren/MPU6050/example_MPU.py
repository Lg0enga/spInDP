# Importeer benodigde libraries
from MPU6050 import MPU6050
import math
from time import sleep

# adc initaliseren met een funcie uit de MPU6050 library
sensor = MPU6050(0x68)

while True:
	accel_data = sensor.get_accel_data()
	gyro_data = sensor.get_gyro_data()
	temp = sensor.get_temp()
	
	#Acceleratie data in xyz richting in variabelen opslaan
	Ax = accel_data['x']
	Ay = accel_data['y']
	Az = accel_data['z']
	#Acceleratie data kwadrateren
	Ax2 = Ax * Ax
	Ay2 = Ay * Ay
	Az2 = Az * Az
	
	#Pitch en roll in radialen berekenen
	Pitchrad = math.atan2(Ax,math.sqrt(Ay2+Az2))
	Rollrad = math.atan2(Ay,math.sqrt(Ax2+Az2))
	#Radialen naar graden omrekenen
	Pitch = math.degrees(Pitchrad)
	Roll = math.degrees(Rollrad)
	
	#Pitch Roll en temperatuur printen
	print("Accelerometer data")
	print("Pitch: " + str(Pitch))
	print("Roll: " + str(Roll))

	print("Temp: " + str(temp) + " C")
	sleep(0.5)