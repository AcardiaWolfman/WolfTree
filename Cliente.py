#!/usr/bin/env python3

import socket
import json

url = input("Introduce la url del servidor de juego ip y puerto separados por dos puntos (x.x.x.x:xxxx)\n")
HOST = url.split(':')[0]
PORT = url.split(':')[1]
print("Conectando a " + HOST + "en el puerto: " + PORT)
buffer_size = 1024
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect((HOST, int(PORT)))
        tam = input("Que tamaño de tablero quieres?\n1)4x4\n2)6x6\n")
        TCPClientSocket.sendall(bytes(tam.encode("utf-8")))
        print("Esperando una respuesta...")
        data = TCPClientSocket.recv(buffer_size)
        tab=json.loads(data.decode())
        print(tab)
        print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())
