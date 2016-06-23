

import time
import GPIO

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

# LED2 GPIO pin

# number of readings at each level
readings_N_total = 3

# pause between readings (s)
reading_pause = 0.3

# pause between steps (s)
step_pause = 0.5

total_time = 2.0 * (step_pause * 200 + reading_pause * readings_N_total * 200) * cycle_N_total


open file
print line (cycle_N	overall_SN,LED1_int,LED2_int,avg_int,reading_N,LDR1_val,LDR2_val,LDR3_val,TSL_val)
close file

start pwm1
start pwm2


for cycle_N in range(1, cycle_N_total+1):
    for light_level in range(0,201):
        for reading_number in range(1,readings_N_total+1):
            # <<<read light levels from sensors>>>
            pause (reading_pause) 
        pause (step_pause)
        
        #increment
        if light_level % 2 == 0: #even light level, so increment LED 1
            PWM1_dc += 1
            set PWM1 dc
        else: # odd light level, so increment LED 2
            PWM2_dc += 1
            set PWM2 dc
    
    for light_level in range(200, -1, -1): # ramp down        

