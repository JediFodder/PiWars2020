import redboard
from time import sleep

servo1=redboard.servo21
servo2=redboard.servo22

#servo1 middle = 8
#servo2 middle = 0

def claws_reset():
    servo1(8)
    servo2(0)

def claws_open():
    servo1(-15)
    servo2(25)


def claws_closed():
    servo1(16)
    servo2(-8)
    


    

sleep(2)
claws_open()
sleep(2)
claws_closed()
    
    

    
