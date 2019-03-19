import maestro
import time
servo = maestro.Controller('/dev/YOURDEVICENAME')
servo.setAccel(1, 4)
servo.setSpeed(1, 10)

'''
left arm:
4000: highest pos
8000: lowest pos
right arm's range is opposite because it's a mirror of the left arm
'''

pos = 1

for x in range(0, 90):
    target_pos = x*pos*100
    print('r:{0}, {1}::{2}'.format(x, target_pos, servo.getPosition(1)))
    servo.setTarget(1, target_pos)
    time.sleep(0.5)

servo.close()
