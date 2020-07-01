import socket

class Cliente:
    HOST = ""
    PORT = 65432

    def init_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s

    def con_sock(self, sock, addr, PORT):
        print(addr)
        print(PORT)
        self.s.connect((addr, PORT))

    def rec_msg(self, sock):
        data = self.s.recv(1024)
        return data.decode("utf-8")

    def rec_mp3(self, sock, file):
        dat=sock.recv(1024)
        n=dat.decode("utf-8")
        f=open(file, "wb")
        for i in range(int(n)):
            data=sock.recv(1024)
            f.write(data)
        f.close()
        return "Ok"
    def __init__(self, Host = "", Port = 7200 ):
        self.s = self.init_socket()
        self.con_sock(self.s,self.HOST,self.PORT)
        reciving = self.rec_msg(self.s)
        print(reciving)
        print(rec_mp3(self.s,"nvo_" + reciving))
#cli= Cliente()
