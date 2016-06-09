# Importeer benodigde libraries
from MPU6050 import MPU6050
import math
from time import sleep

# adc initaliseren met een funcie uit de MPU6050 library
sensor = MPU6050(0x68)

FX = 0
a = 0.95

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
	
	#Gyroscoop data in xyz richting in variabelen opslaan
	Gx = gyro_data['x']
	Gy = gyro_data['y']
	Gz = gyro_data['z']
	
	
	#Berekening hoek gyroscoop
	GX = FX + (Gx/131)*0.05
	
	
	#Pitch en roll in radialen berekenen
	AXrad = math.atan2(Ax,math.sqrt(Ay2+Az2))
	AYrad = math.atan2(Ay,math.sqrt(Ax2+Az2))
	#Radialen naar graden omrekenen
	AX = (math.degrees(AXrad))-3
	AY = math.degrees(AYrad)
	
	FX = a * GX + (1-a)*AX
	
	#Pitch Roll en temperatuur printen
	print("HOEK")
	print("X= " + str(FX))

	sleep(0.05)