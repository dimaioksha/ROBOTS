#!/usr/bin/env python3


from ev3dev.ev3 import *
import math
import time

# Clamps value in the [min, max] range
def clamp(val, _min, _max):
    if val < _min:
        return _min
    if (val > _max):
        return _max
    return val

# Adds +- 2Pi if the difference is larger then Pi
def unwrap(val, previous_val):
    # difference = previous_val - val
    # while difference > math.pi:
    #     val        += math.pi * 2.
    #     difference -= math.pi * 2.
    #     
    # while difference < -math.pi:
    #     val        -= math.pi * 2.
    #     difference += math.pi * 2.
        
    return val

def threshold_clamp(val, _min, _max, threshold_min, threshold_max):
    val = clamp(val, _min, _max)
    if val > threshold_min and val < threshold_max:
        return threshold_max    
    if val < -threshold_min and val > -threshold_max:
        return -threshold_max
    
    if val < threshold_min and val > -threshold_min:
        return 0    
    
    return val

motor_a = LargeMotor('outA')
motor_d = LargeMotor('outD')

inv_wheel_span = 1. / 0.17
wheel_radius = 0.028

linear     = 75
rotational = -200

motor_a.position = 0
motor_d.position = 0

x_goal = 1.
y_goal = 0.5

x_current = 0.
y_current = 0.

theta   = 0.
azimuth = 0.

left_angle  = 0.
right_angle = 0.

dt     = 1.
inv_dt = 1.

time_start = time.time()
while (abs(x_current - x_goal) > 0.1) or (abs(y_current - y_goal) > 0.1):
    motor_a.position = 0
    motor_d.position = 0
    
    x_vec = x_goal - x_current
    y_vec = y_goal - y_current
    
    u_linear = math.sqrt(x_vec ** 2 + y_vec ** 2) * linear
    u_linear = clamp(u_linear, -100, 100)
    
    azimuth = unwrap(math.atan2(y_vec, x_vec), azimuth)
    
    # print("azimuth: {0}, theta: {1}".format(azimuth, theta))
    
    u_rotational = (azimuth - theta) * rotational
    u_rotational = clamp(u_rotational, -100, 100)
    
    u_left  = clamp(u_linear - u_rotational, -100, 100)
    u_right = clamp(u_linear + u_rotational, -100, 100)
    
    # Large motor has 720 pulses per revolutions as stated in https://github.com/ev3dev/ev3dev/issues/148#issuecomment-202498715
    new_left_angle  = motor_a.position * 4 * 0.0174532925199432 
    new_right_angle = motor_d.position * 4 * 0.0174532925199432 # TODO: Check this minus sign
    
    # print("motor_a: {0}, motor_d: {1}".format(motor_a.position, motor_d.position))
    
    # left_speed  = (new_left_angle  - left_angle)  * inv_dt # TODO: Probably this dt's are not needed because they are 
    # right_speed = (new_right_angle - right_angle) * inv_dt # annihilated by the dt's when we are integrating position
    
    left_speed  = new_left_angle  * inv_dt
    right_speed = new_right_angle * inv_dt
    
    left_angle  += new_left_angle
    right_angle += new_right_angle
    
    theta = (left_angle - right_angle) * wheel_radius * inv_wheel_span
    speed = (left_speed + right_speed) * wheel_radius * 0.5

    x_speed = math.cos(theta) * speed
    y_speed = math.sin(theta) * speed
    
    x_current += x_speed * dt # We are integrating position right here
    y_current += y_speed * dt # TODO: Delete this dt's
    
    # print("x_speed: {0}, y_speed: {1}".format(x_speed, y_speed))
    # print("x_current: {0}, y_current: {1}, azimuth: {2}".format(x_current, y_current, azimuth))
    print("x_current: {0}, y_current: {1}, theta: {2}".format(x_current, y_current, theta))
    
    motor_a.run_direct(duty_cycle_sp=int(threshold_clamp(u_left, -100, 100, 5, 45)))
    motor_d.run_direct(duty_cycle_sp=int(threshold_clamp(u_right, -100, 100, 5, 45)))
    
    dt     = time_start - time.time()
    inv_dt = 1. / dt
    
    time_start = time.time()

motor_a.run_direct(duty_cycle_sp=0)
motor_d.run_direct(duty_cycle_sp=0)
