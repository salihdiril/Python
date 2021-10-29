import socket

HOST = "127.0.0.1" # serverın IP adresi
PORT = 65432       # server tarafından kullanılan port

message = input("Mesajınızı yazınız: ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode())
    data = s.recv(1024).decode()

print("Received: ", repr(data))