# import socket module
import socket

# create a socket object
server_socket = socket.socket()

# get local machine name
host = "0.0.0.0"

# reserve a port for your service
port = 12345

# bind to the port
server_socket.bind((host, port))

# enable the server
server_socket.listen(5)

while True:
    # wait and establish connection with client
    conn_socket, addr = server_socket.accept()

    print("Got connection from", addr)
    conn_socket.send(b"Thank you for connecting!\n")
    # close the connection
    conn_socket.close()
