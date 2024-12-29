import network
import socket
import time

# Connect to Wi-Fi
ssid = "Hylke heeft monster"
password = "koekje123"

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

def parse_query_string(query):
    """Parses a URL-encoded query string into a dictionary."""
    params = {}
    for pair in query.split('&'):
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
    return params

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    request_lines = request.decode().splitlines()
    
    if request_lines[0].startswith('POST'):
        for line in request_lines:
            if line.startswith('Content-Length:'):
                content_length = int(line.split(': ')[1])
                break
        else:
            content_length = 0
        body = request[-content_length:] if content_length > 0 else b''
        print("Body:", body.decode())
        if content_length > 0:
            body_str = body.decode()
            parsed_body = parse_query_string(body_str)
            name_value = parsed_body.get('led', '')
            print("Led:", name_value)

    print("Request:", request)

    body = "<iframe src=\"https://kalilinux.org\" width=\"750\ height=\"500\">"
    header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\n\r\n".format(len(body))
    response = header + body
    
    cl.send(response)
    cl.close()
