from gpiozero import AngularServo
from gpiozero import AngularServo
from gpiozero import Servo
from gpiozero.tools import sin_values
from signal import pause
from time import sleep
import math
import serial
import matplotlib.pyplot as plot
import numpy as np


print('Hello')
GP_PIN=18
myCorrection=0.45
#maxPW=(2.0+myCorrection)/1000
#minPW=(1.0-myCorrection)/1000
#minPW = (0.8/1000)
#maxPW = (1.8/1000)
maxPW = (2/1000)
minPW = 1/1000
filter_distance = 100

STARTING_ANGLE = 90
MIN_ANGLE = 40
aServ = AngularServo(GP_PIN, min_angle=0, max_angle=90, min_pulse_width=minPW, max_pulse_width=maxPW)
ser = serial.Serial("/dev/serial0", 115200)
aServ.angle = STARTING_ANGLE
sleep(0.05)

def sweep():
    points = []
    angle = STARTING_ANGLE
    rate_of_change = 0.1
    while True:
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer() 
            # type(recv), 'str' in python2(recv[0] = 'Y'), 'bytes' in python3(recv[0] = 89)
            # type(recv[0]), 'str' in python2, 'int' in python3 	
            distance, strength = 0,0
            if recv[0] == 0x59 and recv[1] == 0x59:     #python3
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                #print('(', distance, ',', strength, ')')
                ser.reset_input_buffer()
                print('(',distance * math.sin(math.radians(angle)), angle,')', 'original dist:',distance, 'angle', angle)
                if distance * math.sin(math.radians(angle)) < filter_distance:
                    points.append([angle,distance * math.sin(math.radians(angle))])
                angle -= rate_of_change
                if angle <= MIN_ANGLE - 1:
                    print('exiting loop, reached max angle of 90')
                    return points
                aServ.angle = angle
                sleep(0.1)

            '''
            if recv[0] == 'Y' and recv[1] == 'Y':     #python2
                lowD = int(recv[2].encode('hex'), 16)      
                highD = int(recv[3].encode('hex'), 16)
                lowS = int(recv[4].encode('hex'), 16)      
                highS = int(recv[5].encode('hex'), 16)
                distance = lowD + highD * 256
                strength = lowS + highS * 256
                print(distance, strength)
            '''
			
            # you can also distinguish python2 and python3: 
            #import sys
            #sys.version[0] == '2'    #True, python2
            #sys.version[0] == '3'    #True, python3

points = sweep()
for i in range(len(points)):
	print(points[i])
xpoints = [points[i][0] for i in range(len(points))]
ypoints = [points[i][1] for i in range(len(points))]
print('xpoints', xpoints)
print('ypoints',ypoints)
# x - theta, y - dsin(x)
#plot.plot(xpoints, ypoints, 'o')
#plot.show()

