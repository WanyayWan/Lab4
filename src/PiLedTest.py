import socket
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
import version as ver

def main():
    # Instantiate and initialize the LCD driver
    if switch == 1:
        led=1
    
    else:
        led=0

if __name__ == "__main__":
    main()
