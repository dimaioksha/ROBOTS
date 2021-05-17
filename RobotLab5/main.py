#!/usr/bin/env python3
from ev3dev.ev3 import *

# Clamps value in the [min, max] range
def clamp(val, _min, _max):
    if val < _min:
        return _min
    if (val > _max):
        return _max
    return val

# Constants:
k1 = -141.82 / 10
k2 = -2.81 / 10
k3 = -25.015 / 10
Umax  = 7.53

# k1 = -3.2005697812446994 # gyro angle
# k2 = -0.5625726007580387 # position
# k3 = -0.7679068687705587 # gyro rate

# k1 = -40
# k2 = 7.03
# k3 = -9.59

# Sensors and motors:
motorA = LargeMotor('outA')
motorB = LargeMotor('outD')
button = TouchSensor('in2')
gyro   = GyroSensor('in3')

# Set the gyro to angle and rate mode
gyro.mode = gyro.MODE_GYRO_G_A

# File logger
logger = open("lab6.txt", 'w')

# Reset the motors
motorA.position = 0
motorB.position = 0

# Main loop varibles:
start_psi     = gyro.angle
start_psi_dot = gyro.rate

while True:
    psi = gyro.angle - start_psi
    
    theta_dot = (motorA.speed + motorB.speed) / 2
    
    psi_dot = gyro.rate - start_psi_dot
    
    U = k1 * psi + k2 * theta_dot + k3 * psi_dot

    logger.write(str(U) + "       " + str(psi) + "        " + str(psi_dot) + "       " + str(motorA.position) + "        " + str(theta_dot) + "\n")
    
    power = clamp(U / Umax * 100, -100, 100)
    
    if not button.is_pressed:
        motorA.run_direct(duty_cycle_sp=power)
        motorB.run_direct(duty_cycle_sp=power)
    else:
        motorA.run_direct(duty_cycle_sp=0)
        motorB.run_direct(duty_cycle_sp=0)
        
        # Reset the loop varibles
        start_psi     = gyro.angle
        start_psi_dot = gyro.rate

    print(str(psi) + "  |   " + str(psi_dot) + " | " + str(gyro.rate))
logger.close()
