import socket

# Localhost'a bağlansın
HOST = "127.0.0.1"
PORT = 65432

# with ifadesi exception handling için kullanılır. Try catch kullanmaktansa with
# kullanmak tercih edilir. with aynı zamanda kapatılması gereken süreçleri de
# kapatır etki alanından çıkınca. Örneğin s.close() yapmadık çünkü with kapatıyor.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # soketi belirli IP ve port numarası ile eşleştirelim
    s.bind((HOST, PORT))

    # bağlantıyı oluşturalım ve bağlantıyı dinleyelim
    s.listen()

    # gelen bağlantıyı kabul edelim
    conn_server, addr = s.accept()
    with conn_server:
        print("Connected by: ", addr)
        while True:
            data = conn_server.recv(1024)
            if not(data):
                break
            reply = "Server says: " + data.decode()
            conn_server.sendall(str.encode(reply))
