#!/usr/bin/python3

"""
Project 1
Names: Lawrence Godfrey
Student Number: GDFLAW001
Prac: Prac 1
Date: <23/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

#sets up GPIO
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    LED_pins = [11,13,15]
    button_pins = [16,18]

    #loop to set up all pins in arrays
    for i in range(len(LED_pins)):
        GPIO.setup(LED_pins[i],GPIO.OUT)

    for i in range(len(button_pins)):
        GPIO.setup(button_pins[i],GPIO.IN)        

    #set up event detect on push buttons for rising edge wih bouncetime 
    GPIO.add_event_detect(16, GPIO.RISING, callback=count_down_callback, bouncetime=250)
    GPIO.add_event_detect(18, GPIO.RISING, callback=count_up_callback, bouncetime=250)

setup()

#counter keeps track of binary 
counter = 0

# callback function when left button is pressed
#increases counter and sets LEDs to new counter value
def count_up_callback(channel):
    global counter
    counter += 1%8
    GPIO.output(11, counter & 0x01)
    GPIO.output(13, counter & 0x02)
    GPIO.output(15, counter & 0x04)
    
#callback function for when right button is pressed
#decreases counter and sets LEDs to new counter value
def count_down_callback(channel):
    global counter
    counter -= 1%8
    GPIO.output(11, counter & 0x01)
    GPIO.output(13, counter & 0x02)
    GPIO.output(15, counter & 0x04)
    
def main():    
    time.sleep(0.1)    
           
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
