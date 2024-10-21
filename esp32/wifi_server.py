import network
import socket
import time

# Connect to Wi-Fi
ssid = "test"
password = "12345678"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Connecting to network...")
    time.sleep(1)

print("Connected to Wi-Fi")
print("IP Address:", wlan.ifconfig()[0])

addr_info = socket.getaddrinfo('0.0.0.0', 80)
addr = addr_info[0][4]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)

print("Listening on", addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    print("Request:", request)

    body = "<iframe src=\"https://kalilinux.org\" width=\"750\ height=\"500\">"
    header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\n\r\n".format(len(body))
    response = header + body
    
    cl.send(response)
    cl.close()
