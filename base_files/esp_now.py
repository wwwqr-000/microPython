import network
import espnow
import time

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)
peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'
e.add_peer(peer)
    
e.send(peer, "Starting...")
for i in range(60000):
    msg = str(i/10)
    print(str(i/10))
    e.send(peer, msg, True)
    time.sleep(0.1)
    
e.send(peer, b'end')
