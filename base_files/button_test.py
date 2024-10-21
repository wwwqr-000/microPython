from machine import Pin
from time import sleep
import screen

buttonL = Pin(23, Pin.IN, Pin.PULL_UP)
buttonR = Pin(18, Pin.IN, Pin.PULL_UP)

x = 10
update = False

screen.drawPixel(x, 20, 1)
screen.refresh()

while True:
    if (buttonL.value() == 0):
        print("Button.Left")
        x -= 1
        update = True
        
    elif (buttonR.value() == 0):
        print("Button.Right")
        x += 1
        update = True
        
    if (update):
        screen.cls()
        screen.drawPixel(x, 20, 1)
        screen.refresh()
        sleep(0.02)
        
