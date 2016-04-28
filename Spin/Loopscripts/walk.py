from ax12 import Ax12
ax12 = Ax12()

from time import sleep

def main():
	speed = 2
	sleeptime = 0.5

	while True:
		ax12.moveSpeed(10, 512, int(1023 * speed))
		ax12.moveSpeed(11, 355, int(491 * speed))
		ax12.moveSpeed(12, 110, int(1021 * speed))

		while (True):
			if ax12.readPosition(10) == 511 and ax12.readPosition(11) == 356 and ax12.readPosition(12) == 109: 
				ax12.moveSpeed(10, 665, int(1023 * speed))
				ax12.moveSpeed(11, 428, int(491 * speed))
				ax12.moveSpeed(12, 263, int(1021 * speed))
				break

		while (True):
			if ax12.readPosition(10) == 664 and ax12.readPosition(11) == 429 and ax12.readPosition(12) == 261:
            			ax12.moveSpeed(11, 467, int(1023 * speed))
            			ax12.moveSpeed(12, 291, int(741 * speed))
				break

		while (True):
			if ax12.readPosition(10) == 664 and ax12.readPosition(11) == 468 and ax12.readPosition(12) == 291:
            			ax12.moveSpeed(10, 512, int(1023 * speed))
            			ax12.moveSpeed(11, 404, int(417 * speed))
            			ax12.moveSpeed(12, 138, int(1018 * speed))
				break

		while(True):
			if ax12.readPosition(10) == 511 and ax12.readPosition(11) == 405 and ax12.readPosition(12) == 138:
            			ax12.moveSpeed(10, 358, int(1023 * speed))
            			ax12.moveSpeed(11, 467, int(417 * speed))
            			ax12.moveSpeed(12, 291, int(1018 * speed))
				break

		while(True):
			if ax12.readPosition(10) == 357 and ax12.readPosition(11) == 468 and ax12.readPosition(12) == 289:
            			ax12.moveSpeed(11, 428, int(417 * speed))
            			ax12.moveSpeed(12, 263, int(1018 * speed))
				break

		while(True):
			if ax12.readPosition(10) == 357 and ax12.readPosition(11) == 429 and ax12.readPosition(12) == 262:
            			ax12.moveSpeed(11, 428, int(417 * speed))
            			ax12.moveSpeed(12, 264, int(1018 * speed))
				break
main()
