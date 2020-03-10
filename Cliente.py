#!/usr/bin/env python3

import socket
import json
import os

url = input("Introduce la url del servidor de juego ip y puerto separados por dos puntos (x.x.x.x:xxxx)\n")
HOST = url.split(':')[0]
PORT = url.split(':')[1]
print("Conectando a " + HOST + "en el puerto: " + PORT)


def x(ca):
    if ca.lower() == "a":
        return 0
    elif ca.lower() == "b":
        return 1
    elif ca.lower() == "c":
        return 2
    elif ca.lower() == "d":
        return 3
    elif ca.lower() == "e":
        return 4
    elif ca.lower() == "f":
        return 5
    else:
        return -1


def imprimeTablero(Tablero, pos1=None, pos2=None):
    os.system("clear")
    i = len(Tablero[0])
    print(
        " ABCD\n" if i == 4 else
        " ABCDEF\n" if i == 6 else ":o"
    )
    y, x = 0, 0
    stri = ""
    if pos1 != None or pos2 != None:
        for fila in Tablero[:-1]:
            stri += str(y + 1)
            for col in fila:
                stri += str(Tablero[pos1[0]][pos1[1]]) if pos1 == [y, x] else str(
                    Tablero[pos2[0]][pos2[1]]) if pos2 == [y, x] else "X"
                x += 1
            y += 1
            print(stri)
            stri = ""
    else:
        for fila in Tablero[:-1]:
            stri += str(y + 1)
            for col in fila:
                stri += "X"
            y += 1
            print(stri)
            stri = ""


buffer_size = 1024

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect((HOST, int(PORT)))
        tam = input("Que tamaño de tablero quieres?\n1)4x4\n2)6x6\n")
        TCPClientSocket.sendall(bytes(tam.encode("utf-8")))
        print("Esperando una respuesta...")
        data = TCPClientSocket.recv(buffer_size)
        # print(data.decode())
        tab = json.loads(data.decode())
        while True:
            Turno = tab[-1]
            imprimeTablero(tab)
            if Turno == "cliente":
                coor = []
                casilla = input("Escribe la coordenada del tablero que quieres voltear (a1 )")
                coor.append(x(casilla[0]))
                coor.append((int(casilla[1]) - 1))
                print(coor)
                imprimeTablero(tab, coor)
                casilla = input("Escribe la coordenada del tablero que quieres voltear (a1 )")
                coor.append(x(casilla[0]))
                coor.append((int(casilla[1]) - 1))
                imprimeTablero(tab, coor)
                TCPClientSocket.sendall(bytes(json.dumps(coor).encode()))
