import lineSensor
import time
import redboard

line = lineSensor.LineSensor(6, 5, 13)

def set_speeds(power_left, power_right):
    """
    As we have an motor hat, we can use the motors
    :param power_left:
    Power to send to left motor
    :param power_right:
    Power to send to right motor, will be inverted to reflect chassis layout
    """
    redboard.M1(-power_right)
    redboard.M2(power_left)

def stop_motors():
    """
    As we have an motor hat, stop the motors using their motors call
    """
    redboard.M1(0)
    redboard.M2(0)
    
 = 100

turn_power = -40


    
while True:
    
    read_line = line.read()
    previous_reading = "000"
    print (read_line)
    reading_string = ""
    if read_line ["left"] == 0:
        reading_string = reading_string + "0"
    else:
        reading_string = reading_string + "1"
        
    if read_line ["middle"] == 0:
        reading_string = reading_string + "0"
    else:
        reading_string = reading_string + "1"
        
    if read_line ["right"] == 0:
        reading_string = reading_string + "0"
    else:
        reading_string = reading_string + "1"

    print(reading_string)
    
    if reading_string == "000":
        print("no line seen")
        reading_string = previous_reading
 
             
        
        
        
        
    if reading_string == "010":
        print("line in middle")
        set_speeds(,)

        
    if reading_string == "011":
        print("line on the right low turn")
        set_speeds(,turn_power)
        
        
    if reading_string == "001":
        print("line on the right more turn")
        set_speeds(,turn_power)
     
    if reading_string == "110":
        print("line on the left low turn")
        set_speeds(turn_power,)
        
        
    if reading_string == "100":
        print("line on the left more turn")
        set_speeds(turn_power,)
        
    if reading_string != "000":
        previous_reading = reading_string
        
    if reading_string == "111":
        stop_motors()
    
    time.sleep(0.05)
    
             
            

    


