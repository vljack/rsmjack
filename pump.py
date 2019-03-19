#!/usr/bin/env python3

import maestro
from time import sleep

LEFT_POS_HI = 4000
LEFT_POS_LO = 7000
RIGHT_POS_HI = 7000
RIGHT_POS_LO = 5000

SERV_LEFT = 0
SERV_RIGHT = 1

accel = 100
speed = 90
wait_factor = 0.3
reps_pump = 50000

servo = maestro.Controller('/dev/YOURDEVICENAME')

def cmd_wait():
    sleep(0.05)
    return

# starting position
servo.setSpeed(SERV_LEFT, 200)
servo.setSpeed(SERV_RIGHT, 200)
cmd_wait()
servo.setAccel(SERV_LEFT, 200)
cmd_wait()
servo.setAccel(SERV_RIGHT, 200)
cmd_wait()
servo.setTarget(SERV_LEFT, LEFT_POS_LO)
cmd_wait()
servo.setTarget(SERV_RIGHT, RIGHT_POS_LO)
cmd_wait()
sleep(1)

while True:
    print('  pump:{0} speed:{1} accel:{2} wait:{3}'.format(x, speed, accel, wait_factor))
    servo.setTarget(SERV_LEFT, LEFT_POS_LO)
    servo.setTarget(SERV_RIGHT, RIGHT_POS_LO)
    cmd_wait()
    sleep(wait_factor)
    servo.setTarget(SERV_LEFT, LEFT_POS_HI)
    servo.setTarget(SERV_RIGHT, RIGHT_POS_HI)
    cmd_wait()
    sleep(wait_factor)

#print(str(servo.getPosition(SERV_LEFT)))
#print(str(servo.getPosition(SERV_RIGHT)))

servo.close()
