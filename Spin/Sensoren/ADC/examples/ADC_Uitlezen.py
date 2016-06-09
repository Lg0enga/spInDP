# Programma welke ADC uitleest en omzet naar ampere of voltage. 
# Author: Kevin Damstra

import time

# Libraries 
import Adafruit_ADS1x15

# adc initaliseren met een funcie uit de ADS1015 Library
adc = Adafruit_ADS1x15.ADS1015()


# Te kiezen versterkingen. 
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V

# Declaraties lists

# List = [Input0, Input1, Input2, Input3] (Indeling onderstaande lists).

GAIN = [2, 2/3, 2/3, 1]						# Input met bijbehorende versterking.
spanning = [2.048, 6.144, 6.144, 4.096]		# Spanning welke bij de gekozen versterking hoort.
deling = [1, 0.4, 0.625, 1]					# Voor sommige inputs is een spanningsdeling toegepast,
                                            # deze moet met de bijbehorende factor weer terug gerekend worden naar de originele waarde. 

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print kolommen
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
# Main loop.
while True:
    # Alle bit waardes worden in een list (bits) gezet waarna ze omgerekend worden naar de bijbehorende eenheid en in een nieuwe list (values) worden gezet.
	values = [0]*4
	bits = [0]*4
	for i in range(4):
        # ADC op de gespecificeerde input lezen.
		bits[i] = adc.read_adc(i, gain=GAIN[i])
		# Omrekening voor kanaal 1 t/m 3.
		if i == 0:
			values[i] = ((bits[i]*(spanning[i]/2048))-0.525)/0.189
		# Omrekening voor kanaal 0.
		else: 
			values[i] = (bits[i]*(spanning[i]/2048))/deling[i]
		
    # Print the ADC waarden.
	print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # Halve seconde pauze.
	time.sleep(0.5)
