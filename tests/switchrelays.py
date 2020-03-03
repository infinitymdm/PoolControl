import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)

for i in range(50):
    gpio.output(3,True)
    time.sleep(1)
    gpio.output(5,True)
    time.sleep(1)
    gpio.output(3,False)
    time.sleep(1)
    gpio.output(5,False)
    time.sleep(1)

gpio.cleanup()