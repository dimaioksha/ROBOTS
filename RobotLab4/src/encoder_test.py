#!/usr/bin/env python3


from ev3dev.ev3 import *
import math
import time

motor_a = LargeMotor('outA')
motor_d = LargeMotor('outD')

motor_a.position = 0
motor_d.position = 0

while True:
	angle_a = motor_a.position * 0.0174532925199432
	angle_d = motor_d.position * 0.0174532925199432
	print("angle_a: {0}, angle_d: {1}, a: {2}, d: {3}".format(angle_a, angle_d, motor_a.position, motor_d.position))