#!/usr/bin/env python3

import socket
import Memoria
import json
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
buffer_size = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("Esperando por jugador")
    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)
        while True:
            print("Esperando a recibir datos... ")
            data = Client_conn.recv(buffer_size)
            dif = str(data.decode("utf-8"))
            print(dif)
            print("4x4" if dif == "1" else "6x6")
            b = True if dif == "1" else False
            x = Memoria.Memoria(b)
            print("Recibido,", data, "   de ", Client_addr)
            if not data:
                break
            print("Enviando respuesta a", Client_addr)
            Client_conn.sendall(bytes(json.dumps(x.Tablero).encode()))
