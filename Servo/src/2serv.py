from gpiozero import Servo
from gpiozero.tools import sin_values
from time import sleep
from signal import pause
import math

PIN = 18
minPW=1/1000
maxPW=2/1000

pi = 3.14
period=90

servo = Servo(PIN,min_pulse_width=minPW, max_pulse_width=maxPW)
servo.value = math.sin(math.radians(90))
sleep(2)



while True:
    choice = input("Enter: ")
    servo.value = int(choice)
    sleep(1)
