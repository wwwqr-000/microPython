from machine import Pin, I2C
from VL53L0X import VL53L0X
from time import sleep

I2C_bus = I2C(0, sda=Pin(19), scl=Pin(23))
ToF = VL53L0X(I2C_bus)

ToF.start()

try:
    while True:
        # Read the distance
        distance = ToF.read()
        print(f"Distance: {distance} mm")
        
        # Wait for a short period
        sleep(0.1)
finally:
    # Stop the sensor on exit
    ToF.stop()
