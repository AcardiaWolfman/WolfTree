import logging
import xmlrpc.client

ok = False
try:
    s = xmlrpc.client.ServerProxy('http://localhost:5432')
    logging.debug("All ok! :)")
    ok = True
except Exception as e:
    e.__cause__

while ok:
    try:
        menu = input("Que quieres hacer?\n"
                     "1) Ver las operaciones del servidor\n"
                     "2) Crear un archivo\n"
                     "3) Renombrar un archivo\n"
                     "4) Eliminar un archivo\n"
                     "5) Crear un directorio\n"
                     "6) Listar un directorio\n"
                     "7) Eliminar un directorio\n"
                     "8) Abrir un archivo\n"
                     "9) Salir\n")
        if menu == "1":
            # Print list of available methods
            print(s.system.listMethods())
        elif menu == "2":
            name = input("Introduce el nombre del archivo: ")
            print(s.create(name))
        elif menu == "3":
            old_name = input("Introduce el nombre actual del archivo: ")
            new_name = input("Introduce el nuevo nombre del archivo: ")
            print(s.rename(name))
        elif menu == "4":
            name = input("Introduce el nombre del archivo: ")
            print(s.rm(name))
        elif menu == "5":
            name = input("Introduce el nombre del directorio: ")
            print(s.mkdir(name))
        elif menu == "6":
            print(s.ls())
        elif menu == "7":
            name = input("Introduce el nombre del directorio: ")
            print(s.rmdir(name))
        elif menu == "8":
            name = input("Introduce el nombre del archivo: ")
            modo = input("Introduce el modo de operacion: ")
            print(s.file(name, modo))
        elif menu == "9":
            ok = False
        else:
            print("opcion invalida")
    except Exception as e:
        print(e.__cause__)
