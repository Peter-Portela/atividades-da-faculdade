import socket
import threading

port = 5050
server = socket.gethostbyname(socket.gethostname())
endereco = (server, port)
format = 'utf-8'
ler_x = "ler x"

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(endereco)

global x
x = ""

def gerenciarCliente(conn, endereco):
    print(f"[nova conexão] {endereco} se conectou.")
    while True:
        global x
        msg = conn.recv(1024).decode(format)
        print (msg)
        if(msg == ler_x):
            conn.send(x.encode(format))
        else:
            x = msg
def iniciar():
    servidor.listen(2)
    print(f"[aguardando] O servidor está aguardando em {server}")
    while True:
        conn, endereco = servidor.accept()
        thread = threading.Thread(target=gerenciarCliente,args =(conn, endereco))
        thread.start()


iniciar()