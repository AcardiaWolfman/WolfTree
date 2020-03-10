#!/usr/bin/env python3

import socket
import threading

import Memoria
import json
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
buffer_size = 1024
def recibir_datos(Client_conn,Client_addr):
    with Client_conn:
        print("Conectado a", Client_addr)
        print("Esperando a recibir datos... ")
        data = Client_conn.recv(buffer_size)
        dif = str(data.decode("utf-8"))
        print(dif)
        print("4x4" if dif == "1" else "6x6")
        b = True if dif == "1" else False
        x = Memoria.Memoria(b)
        print("Recibido,", data, "   de ", Client_addr)
        print("Enviando respuesta a", Client_addr)
        x.Tablero.append("cliente")
        Client_conn.sendall(bytes(json.dumps(x.Tablero).encode()))
        while True:
            data= Client_conn.recv(buffer_size)
            escoge = json.loads(data.decode())
            print(escoge)
            print(escoge[0])
            print(escoge[1])
            print(escoge[2])
            print(escoge[3])
            x.jugador1+=1 if x.validaTurno(escoge[0], escoge[1], escoge[2], escoge[3]) else 0

            #x.jugador2+=1 if x.validaTurno(random()) else

def gestion_conexiones(listaconexiones):
    for conn in listaconexiones:
        if conn.fileno() == -1:
            listaconexiones.remove(conn)
    print("hilos activos:", threading.active_count())
    print("enum", threading.enumerate())
    print("conexiones: ", len(listaconexiones))
    print(listaconexiones)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen(int(input("Numero de jugadores")))
    print("Esperando por jugador")
    Client_conn, Client_addr = TCPServerSocket.accept()
    thread_read = threading.Thread(target=recibir_datos, args=[Client_conn, Client_addr])
    thread_read.start()
