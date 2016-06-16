# Importeer benodigde libraries
from MPU6050 import MPU6050
import math
from time import sleep

# adc initaliseren met een funcie uit de MPU6050 library


sensor = MPU6050(0x68)
i = 0
FX = 0
FY = 0
a = 0.96
gyroScale = 131
while True:
	accel_data = sensor.get_accel_data()
	gyro_data = sensor.get_gyro_data()
	temp = sensor.get_temp()

	#Acceleratie data in xyz richting in variabelen opslaan
	Ax = accel_data['x']
	Ay = accel_data['y']
	Az = accel_data['z']

	print ("Ax = " + str(Ax))

	#Acceleratie data kwadrateren
	Ax2 = Ax * Ax
	Ay2 = Ay * Ay
	Az2 = Az * Az

	#Gyroscoop data in xyz richting in variabelen opslaan
	Gx = gyro_data['x']
	Gy = gyro_data['y']
	Gz = gyro_data['z']


	gsx = Gx / gyroScale
	gsy = Gy / gyroScale
	gsz = Gz / gyroScale



	#Pitch en roll in radialen berekenen
	arx= math.atan2(Ax,math.sqrt(Ay2+Az2))
	ary = math.atan2(Ay,math.sqrt(Ax2+Az2))

	#Radialen naar graden omrekenen
	ARX = math.degrees(arx)
	ARY = math.degrees(ary)

	if i == 0:
		grx = ARX
		gry = ARY

	else:
		grx = grx + (0.05 * gsx)
    		gry = gry + (0.05 * gsy)

	#Berekening hoek gyroscoop
	#GX = (FX + (Gx/gyroScale)*0.05)
	#GY = FY + (Gy/gyroScale)*0.05

	FX = ((a * ARX) + ((1-a)*grx) - 3) * 1.25
	FY = ((a * ARY) + ((1-a)*gry)) * 1.30

	#Pitch Roll en temperatuur printen
	print("HOEK")
	print("X= " + str(FX))
	print("Y= " + str(FY))

	sleep(0.05)
	i+= 1
