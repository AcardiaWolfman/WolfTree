import socket
import os
import selectors
import types

class Servidor:
    HOST = ""
    PORT = 7200
    def init_socket(self,HOST, PORT):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        return s

    def send_mp3(conn, file):
        tam = os.stat(file).st_size
        n=int(tam/1024)
        conn.send(str(n).encode("utf-8"))
        f = open(file, 'rb')
        for i in range(n):
            archivo = f.read(1024)
            conn.send(archivo)
            f.close()
    def send_msg(conn, msg):
        data = msg.encode('utf-8')
        conn.send(data)
    def __init__(self, Host = "", Port = 7200):
        self.HOST = Host
        self.PORT = Port
        self.archivo = "mus.mp3"
        self.s = self.init_socket(self.HOST, self.PORT)
        print("--Server Running--")
        #wait for connection
        while True:
            conn, addr = self.s.accept()
            print("New conection: " + str(addr))
            send_msg(conn, self.archivo)
            send_mp3(conn, self.archivo)
