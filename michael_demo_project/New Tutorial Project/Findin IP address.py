import socket
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)
print("my IP address is " + myip)