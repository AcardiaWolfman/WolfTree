from Servidor import Servidor
from Cliente import Cliente
import threading
def RunAServer():
    servidor = Servidor()
def RunAClient():
    cliente = Cliente()
print("*"*10+"Bienvenido a :"+"*"*10)
print("**************************************************************")
print("         OOOOOO     UU   UU    RRRRRR                         ")
print("        OO    OO    UU   UU    RR   RR                        ")
print("        OO    OO    UU   UU    RR   RR                        ")
print("========OO    OO    UU   UU    RRRRRR   ======================")
print("        OO    OO     U   U     RR   RR                        ")
print("         OOOOOO       UUU      RR    RR                       ")
print("**************************************************************")
print()
print("                         * M U S I C *                        ")
print()
while True:
    menu = input("Que quieres hacer?\n 1) Sólo compartir\n 2) Compartir y descargar\n 3) Sólo descargar\n 4) Salir\n")
    if menu == "1":
        threadServer = threading.Thread(target = RunAServer)
        threadServer.start()
    elif menu == "2":
        threadServer = threading.Thread(target = RunAServer)
        threadServer.start()
        threadClient = threading.Thread(target = RunAClient)
        threadClient.start()
    elif menu == "3":
        threadClient = threading.Thread(target = RunAClient)
        threadClient.start()
    elif menu == "4":
        print("Nos vemos camarada!\n)\\")
        break
#lock = threading.Lock()
#threadServer = threading.Thread(target = RunAServer,args = (lock,))
#threadServer.start()
#threadCliente = threading.Thread(target = RunAClient,args = (lock,))
#threadCliente.start()
