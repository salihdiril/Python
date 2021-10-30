import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    #this means we couldn't resolve the host
    print("there was an error resolving the host")
    sys.exit()

# Connect to server
s.connect((host_ip, port))
print("The socket has successfully connected to google")