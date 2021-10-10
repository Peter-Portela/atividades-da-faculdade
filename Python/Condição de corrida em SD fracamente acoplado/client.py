import socket
import time

port = 5050
server = socket.gethostbyname(socket.gethostname())
endereco = (server, port)
format = 'utf-8'
ler_x = "ler x"

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(endereco)

while True:

    a = 1
    b = 2
    x = a + b
    cliente.send(str(x).encode(format))
    time.sleep(00.5)
    cliente.send(ler_x.encode(format))
    x = cliente.recv(1034).decode(format)
    print("x = " + x)