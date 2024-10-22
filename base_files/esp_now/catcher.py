import network
import espnow
from machine import Pin
from time import sleep

sta = network.WLAN(network.STA_IF)
sta.active(True)
e = espnow.ESPNow()
e.active(True)

allowedClients = ["herman"]
ledPin = Pin(18, Pin.OUT)

def isValidSignal(msg):
    if ('@' not in msg): return False
    global allowedClients
    arr = msg.split('@')
    if (arr[0] not in allowedClients): return False
    return arr[1]
    
ledPin.on()

while True:
    host, msg = e.recv()
    if msg:
        msg = msg.decode("utf-8")
        validRes = isValidSignal(msg)
        if (not isValidSignal(msg)):
            print("Invalid signal...")
            continue
        
        msg = validRes
        if ("on" in msg): ledPin.off()
        else: ledPin.on()
        print(msg)
