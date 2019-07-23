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



# Logic that you write
def main():    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    LED_counter =0
    bit_counter = 0;
    current_num = ""
    LED_pins = [3,5,7]
    button_pins = [8,10]

    for i in range(len(LED_pins)):
        GPIO.setup(LED_pins[i],GPIO.OUT)

    for i in range(len(button_pins)):
        GPIO.setup(button_pins[i],GPIO.IN)
        
    GPIO.output(3, GPIO.HIGH)    
    time.sleep(1)
    GPIO.output(5, GPIO.HIGH)
    
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
