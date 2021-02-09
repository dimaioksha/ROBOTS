#!/usr/bin/env python3


from ev3dev.ev3 import *
import math
import time

# Clamps value in the [min, max] range
def clamp(val: float, _min: float, _max: float)-> float:
    if val < _min:
        return _min
    if (val > _max):
        return _max
    return val

# Adds +- 2Pi if the difference is larger then Pi
def unwrap(val: float, previous_val: float)-> float:
    difference = previous_val - val
    while difference > math.pi:
        val        += math.pi * 2.
        difference -= math.pi * 2.
        
    while difference < -math.pi:
        val        -= math.pi * 2.
        difference += math.pi * 2.
        
    return val

motor_a = LargeMotor('outA')
motor_d = LargeMotor('outD')

inv_wheel_span: float = 1. / 0.16
wheel_radius  : float = 0.056

linear    : float = 5
rotational: float = 10

motor_a.position = 0
motor_d.position = 0

x_goal: float = 2.
y_goal: float = 2.

x_current: float = 0.
y_current: float = 0.

theta  : float = 0.
azimuth: float = 0.

left_angle : float = 0.
right_angle: float = 0.

dt    : float = 1.
inv_dt: float = 1.

time_start = time.time()
while abs(x_current - x_goal) > 0.1 and abs(y_current - x_goal) > 0.1:
    x_vec: float = x_goal - x_current
    y_vec: float = y_goal - y_current
    
    u_linear: float = math.sqrt(x_vec ** 2 + y_vec ** 2) * linear
    u_linear: float = clamp(u_linear, -100, 100)
    
    azimuth = unwrap(math.atan2(y_vec, x_vec), azimuth)
    
    u_rotational: float = (azimuth - theta) * rotational
    u_rotational: float = clamp(u_rotational, -100, 100)
    
    u_left : float = clamp(u_linear - u_rotational, -100, 100)
    u_right: float = clamp(u_linear + u_rotational, -100, 100)
    
    new_left_angle : float = motor_a.position * +0.0174532925199432 
    new_right_angle: float = motor_d.position * -0.0174532925199432  # TODO: Check this minus sign
    
    left_speed : float = (new_left_angle  - left_angle)  * inv_dt # TODO: Probably this dt's are not needed because they are 
    right_speed: float = (new_right_angle - right_angle) * inv_dt # annihilated by the dt's when we are integrating position
    
    left_angle  = new_left_angle
    right_angle = new_right_angle
    
    theta        = (left_angle + right_angle) * wheel_radius * inv_wheel_span
    speed: float = (left_speed + right_speed) * wheel_radius * 0.5

    x_speed: float = math.cos(theta) * speed
    y_speed: float = math.sin(theta) * speed
    
    x_current += x_speed * dt # We are integrating position right here
    y_current += y_speed * dt # TODO: Delete this dt's
    
    motor_a.run_direct(duty_cycle_sp=int(u_left))
    motor_d.run_direct(duty_cycle_sp=int(u_right))
    
    dt     = time_start - time.time()
    inv_dt = 1. / dt
    
    time_start = time.time()

motor_a.run_direct(duty_cycle_sp=0)
motor_d.run_direct(duty_cycle_sp=0)
