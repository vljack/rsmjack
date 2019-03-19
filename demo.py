#!/usr/bin/env python3

import maestro
from time import sleep

# range is 4000/8000 but cap maximum to avoid popoff
LEFT_POS_HI = 5000
LEFT_POS_LO = 7000
RIGHT_POS_HI = 7000
RIGHT_POS_LO = 5500

SERV_LEFT = 0
SERV_RIGHT = 1

accel = 24
speed = 20
wait_factor = 0.55
pump_offset = 1000
right_arm_level_offset = 550

reps_pump = 10
reps_gyrate = 10

servo = maestro.Controller('/dev/YOURDEVICENAME')
#print(str(servo.getPosition(SERV_LEFT)))
#print(str(servo.getPosition(SERV_RIGHT)))

def cmd_wait():
    sleep(0.05)
    return

# starting position
servo.setSpeed(SERV_LEFT, 100)
servo.setSpeed(SERV_RIGHT, 100)
cmd_wait()
servo.setAccel(SERV_LEFT, 40)
cmd_wait()
servo.setAccel(SERV_RIGHT, 40)
cmd_wait()
servo.setTarget(SERV_LEFT, LEFT_POS_LO)
cmd_wait()
servo.setTarget(SERV_RIGHT, RIGHT_POS_LO)
cmd_wait()
sleep(1)


while True:
    accel = accel + 3
    speed = speed + 3
    # values greater than this are pointless for the RSM servos
    if accel > 100:
        accel = 100
    if speed > 128:
        speed > 128

    # avoid negative values
    wait_factor = wait_factor - 0.05
    if wait_factor < 0.25:
        # minimum time for a long range stroke at high speed
        wait_factor = 0.25

    servo.setAccel(SERV_LEFT, accel)
    servo.setAccel(SERV_RIGHT, accel)
    servo.setSpeed(SERV_LEFT, speed)
    servo.setSpeed(SERV_RIGHT, speed)
    cmd_wait()
    #print('accel:{0}, speed:{1}'.format(accel, speed))

    for x in range(1, reps_gyrate):
        print('gyrate:{0} speed:{1} accel:{2} wait:{3:0.1f}'.format(x, speed, accel, wait_factor))
        servo.setTarget(SERV_RIGHT, RIGHT_POS_HI)
        servo.setTarget(SERV_LEFT, LEFT_POS_LO)
        cmd_wait()
        sleep(wait_factor)
        servo.setTarget(SERV_RIGHT, RIGHT_POS_LO)
        servo.setTarget(SERV_LEFT, LEFT_POS_HI)
        cmd_wait()
        sleep(wait_factor)


    # quickly reset to starting position
    servo.setAccel(SERV_LEFT, accel+100)
    servo.setAccel(SERV_RIGHT, accel+100)
    servo.setSpeed(SERV_LEFT, speed+100)
    servo.setSpeed(SERV_RIGHT, speed+100)
    servo.setTarget(SERV_LEFT, LEFT_POS_LO)
    servo.setTarget(SERV_RIGHT, RIGHT_POS_LO)
    sleep(wait_factor)
    # resume previous accel/speed
    servo.setAccel(SERV_LEFT, accel)
    servo.setAccel(SERV_RIGHT, accel)
    servo.setSpeed(SERV_LEFT, speed)
    servo.setSpeed(SERV_RIGHT, speed)

    for x in range(1, reps_pump):
        print('  pump:{0} speed:{1} accel:{2} wait:{3}'.format(x, speed, accel, wait_factor))
        servo.setTarget(SERV_LEFT, LEFT_POS_LO)
        servo.setTarget(SERV_RIGHT, RIGHT_POS_LO)
        cmd_wait()
        sleep(wait_factor)
        servo.setTarget(SERV_LEFT, LEFT_POS_HI)
        servo.setTarget(SERV_RIGHT, RIGHT_POS_HI)
        cmd_wait()
        sleep(wait_factor)

    accel = accel
    servo.setAccel(SERV_LEFT, accel)
    cmd_wait()
    servo.setAccel(SERV_RIGHT, accel)
    cmd_wait()


#print(str(servo.getPosition(SERV_LEFT)))
#print(str(servo.getPosition(SERV_RIGHT)))

servo.close()
