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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

counter = 0

def my_callback_one(channel):
    global counter
    counter += 1%8
    count_up(counter)

def my_callback_two(channel):
    global counter
    counter -= 1%8
    count_down(counter)

LED_pins = [11,13,15]
button_pins = [16,18]

for i in range(len(LED_pins)):
    GPIO.setup(LED_pins[i],GPIO.OUT)

for i in range(len(button_pins)):
    GPIO.setup(button_pins[i],GPIO.IN)        

GPIO.add_event_detect(16,GPIO.RISING,callback=my_callback_two,bouncetime=250)
GPIO.add_event_detect(18,GPIO.RISING,callback=my_callback_one,bouncetime=250)

def main():    
    time.sleep(0.1)    
        
def count_up(counter):
    GPIO.output(11, counter & 0x01)
    GPIO.output(13, counter & 0x02)
    GPIO.output(15, counter & 0x04)
    
def count_down(counter):
    GPIO.output(11, counter & 0x01)
    GPIO.output(13, counter & 0x02)
    GPIO.output(15, counter & 0x04)
        
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
