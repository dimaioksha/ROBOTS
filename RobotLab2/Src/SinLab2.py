#!/usr/bin/env python3


from ev3dev.ev3 import *
import time
import math as m

motor = LargeMotor("outA")

motor.position = 0
data = open("sin_log.txt", "w")

remaining = 0
timeStart = time.time()
while remaining < 10:
	remaining = time.time() - timeStart
	motor.run_direct(duty_cycle_sp=(100 * m.sin(3.1419 * remaining)))
	data.write(str(motor.position) + " " + str(remaining) + "\n")

motor.run_direct(duty_cycle_sp=0)

motor.stop(stop_action="brake")
data.close()

