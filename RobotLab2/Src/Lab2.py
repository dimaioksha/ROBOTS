#!/usr/bin/env python3


from ev3dev.ev3 import *
import time


motor = LargeMotor("outA")

for dutyCycle in range(-100, 101, 10):
	if (dutyCycle == 0):
		continue

	timeStart = time.time()
	motor.position = 0

	data = open("log" + str(dutyCycle) + ".txt", "w")
	data.write("Speed " + str(dutyCycle) + "\n")

	remaining = 0
	while remaining < 1:
		remaining = time.time() - timeStart
		motor.run_direct(duty_cycle_sp=dutyCycle)
		data.write(str(motor.position) + " "+ str(remaining) + "\n")

	motor.run_direct(duty_cycle_sp=0)

	motor.stop(stop_action="brake")
	data.close()

	time.sleep(5)
