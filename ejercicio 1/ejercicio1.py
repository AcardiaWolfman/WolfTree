import socket
import sys
import threading
import random
from datetime import datetime
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# from Server import gestion_conexiones

authenticator = IAMAuthenticator('HuuOkm4voT_3pceZje2oHxhXIZWMX6HepdKWUibJux3H')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(
    'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/751172ec-7304-4eca-9e37-607c6a171ccf')


class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


def traducirVozaTexto():
    myRecognizeCallback = MyRecognizeCallback()

    with open('salser.wav', 'rb') as audio_file:
        audio_source = AudioSource(audio_file)
        speech_to_text.recognize_using_websocket(
            audio=audio_source,
            content_type='audio/wav',
            recognize_callback=myRecognizeCallback,
            model='es-MX_NarrowbandModel',
            keywords=["tiene"],
            keywords_threshold=0.5,
            max_alternatives=1)


        print(speech_to_text.get_model(0))

class AdivinaQuien:
    colores_de_ojos = ["castaño", "ámbar", "avellana", "verde", "azul", "gris"]
    sexos = ["masculino", "femenino"]  # <- Que opresor xD
    tamanio_de_cabello = ["corto", "mediano", "largo"]
    estatura = ["baja", "mediana", "alta"]
    tonos_de_piel = ["claro", "medio", "moreno", "oscura"]
    personajes = []
    caracteristicas = {
        "ojos": ""
        , "cabello": ""  # tamaño
        , "sexo": ""  # <- Helicoptero de guerra piu piu
        , "estatura": ""
        , "piel": ""
        , "nombre": ""
    }

    def Juan(self):
        juan = self.caracteristicas.copy()
        juan["ojos"] = "gris"
        juan["cabello"] = "corto"
        juan["sexo"] = "masculino"
        juan["estatura"] = "mediana"
        juan["piel"] = "moreno"
        juan["nombre"] = "juan"
        return juan

    def Pedro(self):
        pedro = self.caracteristicas.copy()
        pedro["ojos"] = "verde"
        pedro["cabello"] = "mediano"
        pedro["sexo"] = "masculino"
        pedro["estatura"] = "alta"
        pedro["piel"] = "oscura"
        pedro["nombre"] = "Pedro"
        return pedro

    def Carlos(self):
        carlos = self.caracteristicas.copy()
        carlos["ojos"] = "avellana"
        carlos["cabello"] = "corto"
        carlos["sexo"] = "masculino"
        carlos["estatura"] = "mediana"
        carlos["piel"] = "claro"
        carlos["nombre"] = "carlos"
        return carlos

    def Link(self):  # en la descripcion
        link = self.caracteristicas.copy()
        link["ojos"] = "azul"
        link["cabello"] = "largo"
        link["sexo"] = "masculino"
        link["estatura"] = "largo"
        link["piel"] = "clara"
        link["nombre"] = "Link"
        return link

    def Raj(self):
        raj = self.caracteristicas.copy()
        raj["ojos"] = "castaño"
        raj["cabello"] = "corto"
        raj["sexo"] = "masculino"
        raj["estatura"] = "baja"
        raj["piel"] = "moreno"
        raj["nombre"] = "Raj"
        return raj

    def Maria(self):
        maria = self.caracteristicas.copy()
        maria["ojos"] = "castaño"
        maria["cabello"] = "largo"
        maria["sexo"] = "femenino"
        maria["estatura"] = "mediana"
        maria["piel"] = "medio"
        maria["nombre"] = "maria"
        return maria

    def Rosa(self):
        rosa = self.caracteristicas.copy()
        rosa["ojos"] = "verdes"
        rosa["cabello"] = "corto"
        rosa["sexo"] = "femenino"
        rosa["estatura"] = "baja"
        rosa["piel"] = "claro"
        rosa["nombre"] = "rosa"
        return rosa

    def Paola(self):
        paola = self.caracteristicas.copy()
        paola["ojos"] = "ambar"
        paola["cabello"] = "mediano"
        paola["sexo"] = "femenino"
        paola["estatura"] = "alta"
        paola["piel"] = "oscura"
        paola["nombre"] = "paola"
        return paola

    def Veronica(self):
        vero = self.caracteristicas.copy()
        vero["ojos"] = "castaño"
        vero["cabello"] = "corto"
        vero["sexo"] = "femenino"
        vero["estatura"] = "mediana"
        vero["piel"] = "moreno"
        vero["nombre"] = "vero"
        return vero

    def Zelda(self):
        zelda = self.caracteristicas.copy()
        zelda["ojos"] = "azul"
        zelda["cabello"] = "largo"
        zelda["sexo"] = "femenino"
        zelda["estatura"] = "alta"
        zelda["piel"] = "clara"
        zelda["nombre"] = "zelda"
        return zelda

    def __init__(self):
        self.personajes.append(self.Juan())
        self.personajes.append(self.Carlos())
        self.personajes.append(self.Link())
        self.personajes.append(self.Pedro())
        self.personajes.append(self.Raj())
        self.personajes.append(self.Maria())
        self.personajes.append(self.Veronica())
        self.personajes.append(self.Zelda())
        self.personajes.append(self.Paola())
        self.personajes.append(self.Rosa())

    def EscogerPersonaje(self):
        self.personajes.shuffle()
        return self.personajes[0]

    def ImprimirPersonajes(self):
        for personaje in self.personajes:
            print("-------------------------------------")
            print("Nombre: " + personaje["nombre"])
            print("Ojos: " + personaje["ojos"])
            print("Cabello: " + personaje["cabello"])
            print("Sexo: " + personaje["sexo"])
            print("Estatura: " + personaje["estatura"])
            print("Piel: " + personaje["piel"])
            print("-------------------------------------")


buffer_size = 1024


def servirPorSiempre(socketTcp, listaconexiones):
    try:
        while True:
            client_conn, client_addr = socketTcp.accept()
            print("Conectado a", client_addr)
            listaconexiones.append(client_conn)
            thread_read = threading.Thread(target=recibir_datos, args=[client_conn, client_addr])
            thread_read.start()
            gestion_conexiones(listaConexiones)
    except Exception as e:
        print(e)


def gestion_conexiones(listaconexiones):
    for conn in listaconexiones:
        if conn.fileno() == -1:
            listaconexiones.remove(conn)
    print("hilos activos:", threading.active_count())
    print("enum", threading.enumerate())
    print("conexiones: ", len(listaconexiones))
    print(listaconexiones)


def recibir_datos(client_conn, client_addr):
    try:
        cur_thread = threading.current_thread()
        print("Recibiendo datos del cliente {} en el {}".format(client_addr, cur_thread.name))
        # -------------------------------------------------------------------------------------------------------------
        while True:
            # archivo de voz
            voz = open("salser.wav", "wb")
            recdata = client_conn.recv(buffer_size)
            while recdata:
                voz.write(recdata)
                recdata = client_conn.recv(buffer_size)
            print("recdata es")
            print(recdata)

            voz.close()
            traducirVozaTexto()
            input()
            # ibm tts

            # data = client_conn.recv(buffer_size) #recibe
            # men = ""
            # client_conn.sendall(men.encode('utf-8') #envia men
            # print("Esperando a recibir datos...")

        # -------------------------------------------------------------------------------------------------------------

    except Exception as e:
        print(e)
    finally:
        client_conn.close()


listaConexiones = []
# host, port, numConn = sys.argv[1:4]
host = "127.0.0.1"
port = "65432"
numConn = "1"
# if len(sys.argv) != 4:
#    print("usage:", sys.argv[0], "<host> <port> <num_connections>")
#    sys.exit(1)

serveraddr = (host, int(port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    # TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPServerSocket.bind(serveraddr)
    TCPServerSocket.listen(int(numConn))
    print("El servidor TCP está disponible y en espera de " + numConn + " solicitudes")

    servirPorSiempre(TCPServerSocket, listaConexiones)
