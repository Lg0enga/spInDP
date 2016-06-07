# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import atexit


# Import the PCA9685 module.
import Adafruit_PCA9685

class DriveServos(object):

    def __init__(self):
        # Uncomment to enable debug output.
        #import logging
        #logging.basicConfig(level=logging.DEBUG)

        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()

        # Alternatively specify a different address and/or bus:
        #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

        # Configure min and max servo pulse lengths
        self.frequency = 40 # frequency
        self.period = 1000000 / self.frequency
        bits = 4096
        self.time_per_tick = self.period / bits
        pulseTimeMin = 900
        pulseTimeMid = 1500
        pulseTimeMax = 2100
        self.servo_min = int(pulseTimeMin / self.time_per_tick)  # Min pulse length out of 4096
        self.servo_mid = int(pulseTimeMid/ self.time_per_tick) # Mid pulse length out of 4096
        self.servo_max = int(pulseTimeMax / self.time_per_tick) # Max pulse length out of 4096
        self.pulseTimeDeltaMax = (self.servo_max - self.servo_min) / 2
        self.pulseTimeDeltaMin = -self.pulseTimeDeltaMax
        self.oldMin = -1023
        self.oldMax = 1023
        self.centerX = 0
        self.centerY = 0
        self.deadzone = 100
        self.pwm.set_pwm_freq(self.frequency)
        self.move = 0
        self.turn = 0

        self._driveServoRightPulseTime = 0
        self._driveServoLeftPulseTime = 0

    # Helper function to make setting a servo pulse width simpler.
    #def set_servo_pulse(channel, pulse):
    #    pulse_length = 1000000    # 1,000,000 us per second
    #    pulse_length //= 60       # 60 Hz
    #    print('{0}us per period'.format(pulse_length))
    #    pulse_length //= 4096     # 12 bits of resolution
    #    print('{0}us per bit'.format(pulse_length))
    #    pulse *= 1000
    #    pulse //= pulse_length
    #    pwm.set_pwm(channel, 0, pulse)

    #def set_mid_pulse(self):
    #    pwm.set_pwm(0, 0, servo_mid)
    #    print("arrived")

    def map(self, oldValue):
        oldRange = (self.oldMax - self.oldMin)
        newRange = (self.pulseTimeDeltaMax - self.pulseTimeDeltaMin)
        return (((oldValue - self.oldMin) * newRange) / oldRange) + self.pulseTimeDeltaMin
    # Set frequency to 60hz, good for servos.
    #self.pwm.set_pwm_freq(self.frequency)
    #def printStuff(self):
        #print self.period
        #print self.servo_min
        #print self.servo_max
        #print self.time_per_tick
        #print map(self, 200)

    def drive(self, xSpeed, ySpeed):
        # print "test"
        # atexit.register(self.pwm.set_pwm(0, 0, 246))
        # atexit.register(self.pwm.set_pwm(1, 0, 246))

        # Move servo on channel O between extremes.
        if ySpeed <= self.centerY - self.deadzone or ySpeed >= self.centerY + self.deadzone:
            move = self.map(ySpeed)
        else:
            move = 0
        if xSpeed <= self.centerX - self.deadzone or xSpeed >= self.centerX + self.deadzone:
            turn = self.map(xSpeed)
        else:
            turn = 0
        driveServoRightPulseTime = self.servo_mid + move + turn
        driveServoLeftPulseTime = self.servo_mid - move + turn

        self._driveServoRightPulseTime = driveServoRightPulseTime
        self._driveServoLeftPulseTime = driveServoLeftPulseTime

        print self._driveServoRightPulseTime, self._driveServoLeftPulseTime

        self.pwm.set_pwm(0, 0, int(self._driveServoRightPulseTime))
        self.pwm.set_pwm(1, 0, int(self._driveServoLeftPulseTime))
