# Importeer benodigde libraries
from MPU6050 import MPU6050
import math
from time import sleep
# adc initaliseren met een funcie uit de MPU6050 library


class GyroData(object):
	def __init__(self):
		self.sensor = MPU6050(0x68)
		self.FX = 0
		self.FY = 0
		self.a = 0.5
		self.gyroScale = 131
		self.grx = 0
		self.gyx = 0

	def getGyroDataX(self, iterator):
		accel_data = self.sensor.get_accel_data()
		gyro_data = self.sensor.get_gyro_data()
		temp = self.sensor.get_temp()

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

        #Berekening hoek gyroscoop
		gsx = Gx / self.gyroScale

		#Pitch en roll in radialen berekenen
		arx= math.atan2(Ax,math.sqrt(Ay2+Az2))

		#Radialen naar graden omrekenen
		ARX = math.degrees(arx)

		if iterator == 0:
			self.grx = ARX
		else:
			self.grx = self.grx + (1 * gsx)

		#Pitch Roll en temperatuur printen

		self.FX = ((self.a * ARX) + ((1-self.a)*self.grx) - 4) * 1.3

		return float(round(self.FX))

	def getGyroDataY(self, iterator):
        	accel_data = self.sensor.get_accel_data()
        	gyro_data = self.sensor.get_gyro_data()
        	temp = self.sensor.get_temp()

        #Acceleratie data in xyz richting in variabelen opslaan
		Ax = accel_data['x']
        	Ay = accel_data['y']
        	Az = accel_data['z']

        #Acceleratie data kwadrateren
		Ax2 = Ax * Ax
        	Ay2 = Ay * Ay
        	Az2 = Az * Az

        #Gyroscoop data in xyz richting in variabelen opslaan
        	Gy = gyro_data['y']

        #Berekening hoek gyroscoop
        	gsy = Gy / self.gyroScale

		#Pitch en roll in radialen berekenen
        	ary = math.atan2(Ay,math.sqrt(Ax2+Az2))

        #Radialen naar graden omrekenen
        	ARY = math.degrees(ary)

		if iterator == 0:
			self.gry = ARY
		else:
			self.gry = self.gry + (1 * gsy) * 1.3
		#Pitch Roll en temperatuur printen


		self.FY = ((self.a * ARY) + ((1-self.a)*self.gry))
		return float(round(self.FY))
