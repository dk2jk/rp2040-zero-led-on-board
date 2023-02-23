#main.py

print('main...')

from led_on_board import Led_on_board
import time

led=Led_on_board()

def led_demo():   
    for _i in range(4):
        time.sleep(.5)
        led.red()
        time.sleep(.5)
        led.green()
        time.sleep(.5)
        led.blue()
    led(0)
    for i in range (4):
        time.sleep(.5)
        led(1)
        time.sleep(.5)
        led(0)
while True:
    led_demo()
