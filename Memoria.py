#!/usr/bin/env python3
from random import randint
from time import sleep
import sys


class Memoria:
    Tablero = []
    dim = 4
    cartas = []
    usadas = []
    el = 0
    jugador1 = 0
    jugador2 = 0

    def iniTab(self):
        i = 0
        if self.dim == 4:
            while i < self.dim:
                self.Tablero.append([-1, -1, -1, -1])
                i += 1
        elif self.dim == 6:
            while i < self.dim:
                self.Tablero.append([0, 0, 0, 0, 0, 0])
                i += 1

    def validaTurno(self, x1, y1, x2, y2):
        if [x1, y1] in self.usadas or [x2, y2] in self.usadas:
            return False
        t = self.Tablero[y1][x1] == self.Tablero[y2][x2]
        if t:
            self.usadas.append([x1, y1], [x2, y2])
        return t

    def AsignaCasilla(self, carta):
        if self.dim == 4:
            while True:
                x = randint(0, 3)
                y = randint(0, 3)
                if self.Tablero[x][y] == -1:
                    self.Tablero[x][y] = carta
                    break
        elif self.dim == 6:
            while True:
                x = randint(0, 5)
                y = randint(0, 5)
                if self.Tablero[x][y] == -1:
                    self.Tablero[x][y] = carta
                    break

    def __init__(self, tam, cole=0):
        dim = 4 if tam else 6
        tam = 8 if dim == 4 else 18
        self.iniTab()
        print(self.Tablero)
        cart = range(0, tam)
        print(cart)
        for c in cart:
            self.AsignaCasilla(c)
            self.AsignaCasilla(c)
        print(self.Tablero)
