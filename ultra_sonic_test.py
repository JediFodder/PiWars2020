from gpiozero import DistanceSensor
from time import sleep
ultrasonic = DistanceSensor(echo=10, trigger=11)

while True:
    sleep (0.1)
    print(ultrasonic.distance)
