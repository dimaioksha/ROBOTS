#!/usr/bin/env python3
from ev3dev.ev3 import *

import math

motorA = LargeMotor('outA')
motorD = LargeMotor('outD')

B = 0.28
r = 0.056
Umax = 500
pwr_str = 0
pwr_rot = 0
kp_str = 500
kp_rot = 100
Xfinal = -1
Yfinal = -1
xcur = 0
ycur = 0
xprev = xcur
yprev = ycur
Qcur = 0
Qprev = Qcur
Qfinal = 0
coordinate = 0.7

error = 0.02

fh = open('lab4.txt', 'w')
motorD.position = 0
motorA.position = 0

for i in range(5):
    Xfinal = coordinate
    Yfinal = coordinate

    if (i == 1):
        Xfinal = -coordinate
        Yfinal = coordinate
    if (i == 2):
        Xfinal = -coordinate
        Yfinal = -coordinate
    if (i == 3):
        Xfinal = coordinate
        Yfinal = -coordinate
    if (i == 4):
        Xfinal = coordinate
        Yfinal = coordinate

    while (abs(xcur - Xfinal) > error or abs(ycur - Yfinal) > error):
        xcur = xcur + math.cos(Qcur) * r * (motorA.position + motorD.position) / 2 * 2 * math.pi / 360
        ycur = ycur - math.sin(Qcur) * r * (motorA.position + motorD.position) / 2 * 2 * math.pi / 360

        p = math.sqrt(math.pow((Xfinal - xcur), 2) + math.pow((Yfinal - ycur), 2))

        Qcur = Qcur + (motorA.position - motorD.position) * r / B / 360 * 2 * math.pi

        if (xcur - Xfinal == 0):
            if (ycur - Yfinal > 0):
                Qfinal = -math.pi / 2
            else:
                Qfinal = math.pi / 2

        if (xcur - Xfinal > 0):
            Qfinal = (math.pi - math.atan2((ycur - Yfinal), (xcur - Xfinal)))
        if (xcur - Xfinal < 0):
            Qfinal = math.atan(-(ycur - Yfinal) / (xcur - Xfinal))

        if (Qfinal > math.pi and abs(xcur - Xfinal) < 2 and abs(ycur - Yfinal) > 2 and i != 4):
            Qfinal = Qfinal - math.pi * 2
        if (Qfinal > math.pi and abs(xcur - Xfinal) < 2 and i == 4):
            Qfinal = Qfinal - math.pi * 2
        pwr_str = Umax * math.tanh(p) * math.cos(Qfinal - Qcur)

        pwr_rot = kp_rot * (Qfinal - Qcur) + Umax * math.tanh(p) / p * math.sin(Qfinal - Qcur) * math.cos(Qfinal - Qcur)

        if (pwr_str > 60):
            pwr_str = 60
        if (pwr_str < -60):
            pwr_str = -60

        if (pwr_rot > 40):
            pwr_rot = 40
        if (pwr_rot < -40):
            pwr_rot = -40

        motorA.position = 0
        motorD.position = 0
        motorD.run_direct(duty_cycle_sp=pwr_str - pwr_rot)
        motorA.run_direct(duty_cycle_sp=pwr_str + pwr_rot)
        fh.write(str(xcur) + ' ' + str(ycur) + '\n')
        # xprev = xcur
        # yprev = ycur
        # Qprev = Qcur
    Qcur = Qfinal
fh.close()
