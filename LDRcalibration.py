#!/usr/bin/env python

print("hello world")

import time
import datetime
#import GPIO
import math
#import spidev
import os
import datetime
#import tsl_2561_bechhofer_low as TSL
#import randomgen

'''
# For MCP3008
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7

# Read SPI (MCP3008, 10-bit ADC)
def readchannel(channel):
    """docstring for readchannel"""
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data
    
# To read the TSL2561, use TSL.readLux(1)
'''



    
# output filename
filename = "output.csv"

# number of complete cycles (ramp up and down)
cycle_N_total = 3

# PWM1 frequency
PWM1_f = 60

# PWM1 duty cycle
PWM1_dc = 0

# PWM2 frequency
PWM2_f = 60

# PWM2 duty cycle
PWM2_dc = 0

# LED1 GPIO pin
LED1_pin = 1

# LED2 GPIO pin
LED2_pin = 2

# number of readings at each level
readings_N_total = 3

# pause between readings (s)
reading_pause = 0.1

# pause between steps (s)
step_pause = 0.04

total_time = 2.0 * (step_pause * 200 + reading_pause * readings_N_total * 200) * cycle_N_total
print('total time %s seconds') % total_time
time_start = datetime.datetime.now()

f = open(filename, 'w')
#f.write('cycle_N,overall_SN,LED1_int,LED2_int,avg_int,reading_N,LDR1_val,LDR2_val,LDR3_val,TSL_val\n')
f.write('cycle_N,cycle_N_total,light_level,reading_number,PWM1_dc,PWM2_dc\n')
f.close

#start pwm1
#start pwm2


for cycle_N in range(1, cycle_N_total+1):
    for light_level in range(0,200):
        for reading_number in range(1,readings_N_total+1):
            # <<<read light levels from sensors, and write>>>
            f = open(filename, 'a')
            random_number = randomgen.rannum(100)
            str = ('%s,%s,%s,%s,%s,%s\n') % (cycle_N, random_number, light_level, reading_number, PWM1_dc, PWM2_dc)
            f.write(str)
            f.close
            time.sleep(reading_pause) 
        time.sleep(step_pause)
        
        #increment
        if light_level % 2 == 0: #even light level, so increment LED 1
            PWM1_dc += 1
            #set PWM1 dc
        else: # odd light level, so increment LED 2
            PWM2_dc += 1
            #set PWM2 dc
    
    for light_level in range(200, 0, -1): # ramp down
        for reading_number in range(1,readings_N_total+1):
            # <<<read light levels from sensors, and write>>>
            f = open(filename, 'a')
            str = ('%s,%s,%s,%s,%s,%s\n') % (cycle_N, cycle_N_total, light_level, reading_number, PWM1_dc, PWM2_dc)
            f.write(str)
            f.close
            time.sleep(reading_pause) 
        time.sleep(step_pause)
        
        #increment
        if light_level % 2 == 0: #even light level, so increment LED 1
            PWM1_dc -= 1
            #set PWM1 dc
        else: # odd light level, so increment LED 2
            PWM2_dc -= 1
            #set PWM2 dc

time_finish = datetime.datetime.now()
print('total time elapsed is %s') % (time_finish - time_start)
