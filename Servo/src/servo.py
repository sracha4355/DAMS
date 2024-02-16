from gpiozero import AngularServo
from gpiozero import Servo
from gpiozero.tools import sin_values
from signal import pause
from time import sleep

# NOTE: servo is only able to rotate 90 degrees with this configuration
# any other pulse width results in inaccurate results
# there may be a configuration that can work
# NOTE FOR SELF: min pulse width = 1ms, max pulse width = 2ms, range 0-90 degrees

GP_PIN=18
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

maxPW = (2/1000)
minPW = 1/1000
#minPW = (0.8/1000)
#maxPW = (1.8/1000)

print(minPW, maxPW)
#serv = Servo(GP_PIN, min_pulse_width=minPW, max_pulse_width=maxPW)
aServ = AngularServo(GP_PIN, min_angle=0, max_angle=90, min_pulse_width=minPW, max_pulse_width=maxPW)

currentAngle = 0
aServ.angle = 0
sleep(0.5)
'''
while currentAngle < 90:
    print('moving to', currentAngle)
    aServ.angle = currentAngle
    currentAngle += 0.10
    sleep(0.05)
'''

while True:
    choice = input("enter: ")
    if choice == "min":
        aServ.angle = 0
    elif choice == "max":
        aServ.angle = 180
    elif choice == "mid":
        aServ.angle = 90
    else:
        aServ.angle = int(choice)
    sleep(1)
        

'''
while True:
    serv.min()
    sleep(1)
    serv.mid()
    sleep(1)
    serv.max()
    sleep(1)
    serv.mid()
    sleep(1)


while True:
    choice = input("choose dir: ")
    if choice == "min":
        serv.min()
    elif choice == "max":
        serv.max()
    elif choice == "mid":
        serv.mid()
    elif choice == "one piece is mid":
        serv.min()
        sleep(0.05)
        serv.max()
        sleep(0.05)
        serv.mid()
        sleep(0.05)
        serv.min()
    else:
        print('wrong choice')
    sleep(0.05)

''' 


	


