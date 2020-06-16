import socket
import pyaudio
import wave
from scipy.io import wavfile
import sounddevice


class Grabadora:
    def __init__(self, fs=44100, canales=64, dtipo='float64'):
        self.fs = fs
        print(fs)
        #sounddevice.default.device = 8
        sounddevice.default.samplerate = fs
        sounddevice.default.channels = 1
        sounddevice.default.dtype = dtipo

    def grabar(self, duracion=3, zoom=10):
        print("Grabando...")
        muestras = sounddevice.rec(int(duracion * self.fs))
        sounddevice.wait()
        print("Listo!!")
        wavfile.write("output.wav", self.fs, muestras)


# -------------------------------------------
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
buffer_size = 1024
grabadora = Grabadora()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    print("Conexion establecida...")

    op = input()
    TCPClientSocket.sendall(op.encode('utf-8'))

    x = 0
    y = 0
    while True:
        # data = TCPClientSocket.recv(buffer_size) #recibe
        # print(data.decode('utf-8'))
        # x = input() envia
        # TCPClientSocket.sendall(x.encode('utf-8'))

        # ---------------------------voz-*-------------------------
        # if es_turno:
        if True:
            grabadora.grabar()
            voz = open("output.wav", "rb")
            SD = voz.read()
            TCPClientSocket.sendall(SD)

            break
        # ---------------------------------------------------------
