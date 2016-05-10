from ax12 import Ax12
ax12 = Ax12()

import time
def main():
	#speed = 1
	#ax12.setID(1, 10)

	#ax12.learnServos()
#	while True:
#		time.sleep(3)
		ax12.moveSpeed(20, 725, 300)
		ax12.moveSpeed(21, 30, 300)
		time.sleep(3)
		ax12.moveSpeed(20, 30, 300)
		ax12.moveSpeed(21, 725, 300) 
		time.sleep(2)
        #ax12.moveSpeed(11, 210, int(2046 * speed))
        #ax12.moveSpeed(12, 69, int(2046 * speed))

	#ax12.setTorqueStatus(10, False)
	#ax12.setTorqueStatus(11, False)
	#ax12.setTorqueStatus(12, False)

	#while True:
	#	print ax12.readPosition(10)
	#	print ax12.readPosition(11)
	#	print ax12.readPosition(12)

#	while True:
#		ax12.readPosition(12)
	#while True:
		#ax12.moveSpeed(10, 512, 100)	
		#ax12.moveSpeed(11, 512, 50)
		#time.sleep(1)
		#ax12.moveSpeed(12, 512, 50)
		#time.sleep(2)
		#print ax12.readPosition(12) 
		#ax12.move(10, 300)
		#time.sleep(1)
		##print ax12.move(10, 400)
		#ax12.move(11, 350)
		#ax12.moveSpeed(12, 300, 200)
		#ax12.move(10, 700)
		#time.sleep(2)
		#ax12.move(12, 700)
		#ax12.moveSpeed(11, 650, 200)
		#time.sleep(1)
		#ax12.move(10, 512)
		#ax12.move(12, 512)
		#ax12.moveSpeed(11, 512, 200)
	#testVar = input("graden")

#	ax12.setID(7,10)
#	ax12.setID(14,11)
#	ax12.setID(1,12)

#	ax12.learnServos()
	#print ax12.readPosition(7)

	#x = 1
	#while True:
	#	ax12.move(1,x)
	#	ax12.move(7,x)
	#	x += 10
	#	print ax12.readPosition(1)
	#	print ax12.readPosition(7)
	#ax12.ping(7)
	#print ax12.readPosition(7)
	#print ax12.readSpeed(7)
	#ax12.moveSpeed(7, 1023, 2047)
	#print ax12.readPosition(7)
	#print ax12.readVoltage(7)
	#print degree(testVar)
def degree(T):
    	oldRange = (0 - 300)
	newRange = (0 - 1024)

	return (((T - 299) * newRange) / oldRange) + 1023

main()
