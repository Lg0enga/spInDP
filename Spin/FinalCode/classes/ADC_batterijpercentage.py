# Programma welke ADC uitleest en omzet naar ampere of voltage.
# Author: Kevin Damstra

import time

# Libraries
import Adafruit_ADS1x15

# adc initaliseren met een funcie uit de ADS1015 Library
class BatteryPercentage(object):
    def __init__(self):

        self.adc = Adafruit_ADS1x15.ADS1015()
        self.i = 0
        self.oldRange = 18000
        self.newRange = 100
        self.spanning = False
        self.GAIN = [2, 2/3]					# Input met bijbehorende versterking.
        self.spanning = [2.048, 6.144]	        # Spanning welke bij de gekozen versterking hoort.
        self.deling = [1, 0.4]	        # Voor sommige inputs is een spanningsdeling toegepast,
        self.percentage = 0                 # deze moet met de bijbehorende factor weer terug gerekend worden naar de originele waarde.

    def calculatePercentage(self):
        while True:
            if self.spanning == True:
                bits = self.adc.read_adc(1, gain=self.GAIN[1])
                values = (bits*(self.spanning[1] / 2048))/self.deling[1]
            else:
                bits = self.adc.read_adc(0, gain=self.GAIN[0])
                values = ((bits * (self.spanning[0] / 2048)) - 0.525) / 0.189
            coulomb = values * self.i
            self.percentage = self.newRange - ((coulomb * self.newRange) / self.oldRange)
            time.sleep(1)
            self.i+=1

    def getPercentage(self):
        return self.percentage
