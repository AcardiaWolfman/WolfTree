import socket
import pyaudio
import wave


class voz:
    def __init__(self):
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 2
        fs = 44100  # Record at 44100 samples per second
        seconds = 3
        filename = "output.wav"
        p = pyaudio.PyAudio()  # Create an interface to PortAudio

    def grabar(self):
        print('Recording')

        stream = self.p.open(format=self.sample_format,
                             channels=self.channels,
                             rate=self.fs,
                             frames_per_buffer=self.chunk,
                             input=True)

        frames = []  # Initialize array to store frames
        # Store data in chunks for 3 seconds
        for i in range(0, int(self.fs / self.chunk * self.seconds)):
            data = stream.read(self.chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        self.p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(frames))
        wf.close()


# -------------------------------------------
HOST = "8.40.1.237"  # The server's hostname or IP address
PORT = 1234  # The port used by the server
buffer_size = 1024
vozobj = voz()
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
            vozobj.grabar()
            voz = open("output.wav", "rb")
            SD = voz.read()
            TCPClientSocket.sendall(SD)
        # ---------------------------------------------------------
