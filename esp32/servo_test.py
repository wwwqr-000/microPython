import machine, time

p23 = machine.Pin(23, machine.Pin.OUT)
servo = machine.PWM(p23, freq=50)
r = 20

rEnd = 135

pB1 = machine.Pin(21, machine.Pin.IN)

while True:
    
    if (pB1.value() == 1):
        print("test")
        time.sleep(0.5)
        


"""
#while True:
    servo.duty(r)
    if (r == 20):
        time.sleep(1)
    r += 1
    print(r)
    time.sleep(0.005)
    if (r == 130):
        r = 20
"""
