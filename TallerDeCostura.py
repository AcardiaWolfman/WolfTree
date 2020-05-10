import threading, time, logging

telas = ["Azul", "Rojo", "Negro", "Morado", "Naranja", "Verde", "Blanco", "Café con leche cosmico"]


def persona_mangas(lock, cesta, tamCesta, telas, sleepTime=4):
    while True:
        print("cesta"+str(cesta)+str(type(cesta)))
        print("tamCesta"+str(tamCesta)+str(type(tamCesta)))
        print("Telas"+str(telas)+str(type(telas)))

        if not lock.locked():
            ces = len(cesta)
            if ces <= tamCesta:
                lock.acquire()
                logging.debug("Fabricando mangas")
                time.sleep(sleepTime)
                telas.shuffle()
                cesta.append(telas[0])
                lock.release()
            else:
                logging.debug("Cesta llena")
                time.sleep(sleepTime / 2)
        else:
            logging.debug("Cesta ocupada")
            time.sleep(sleepTime / 2)


def persona_cuerpo(lock, cesta, tamCesta, telas, sleepTime=2):
    while True:
        if not lock.locked():
            ces = len(cesta)
            if ces <= tamCesta:
                lock.acquire()
                logging.debug("Fabricando cuerpo")
                time.sleep(sleepTime)
                telas.shuffle()
                cesta.append(telas[0])
                lock.release()
            else:
                logging.debug("Cesta llena")
                time.sleep(sleepTime / 2)
        else:
            logging.debug("Cesta ocupada")
            time.sleep(sleepTime / 2)


def persona_ensambladora(lock, cestaMangas, cestaCuerpos, sleepTime=4):
    while True:
        if not lock.locked():
            cesm = len(cestaMangas)
            cesc = len(cestaCuerpos)
            if cesm >= 2 & cesc >= 1:
                lock.acquire()
                logging.debug("Creando prenda")
                time.sleep(sleepTime)
                cestaMangas.shuffle()
                cestaCuerpos.shuffle()
                logging.debug(
                    "Prenda de mangas: " + cestaMangas[0] + " y " + cestaMangas[1] + " con cuerpo " + cestaCuerpos[0])
                cestaMangas.remove(0)
                cestaMangas.remove(1)
                cestaCuerpos.remove(1)
                lock.release()
            else:
                logging.debug("Faltan mangas o cuerpos")
                time.sleep(sleepTime / 2)
        else:
            logging.debug("Cestas ocupada")
            time.sleep(sleepTime / 2)


lockM = threading.Lock()
lockC = threading.Lock()
lockE = threading.Lock()
pm = int(input("Personas haciendo mangas? \n"))
pc = int(input("Personas haciendo cuerpos? \n"))
pe = int(input("Personas haciendo ensamblando? \n"))
barrier = threading.Barrier(pm)
barrier = threading.Barrier(pc)
barrier = threading.Barrier(pe)
cestaMangas = []
cestaCuerpos = []
mangakas = [threading.Thread(name='worker-%s' % i, target=persona_mangas, args=(lockM, cestaMangas, 50, telas), )
            for i in range(pm)]
cuerposf = [threading.Thread(name='worker-%s' % i, target=persona_cuerpo, args=(lockC, cestaCuerpos, 50, telas), )
            for i in range(pc)]
ensambladores = [
    threading.Thread(name='worker-%s' % i, target=persona_cuerpo, args=(lockE, cestaMangas, cestaCuerpos, 50), )
    for i in range(pe)]
for m in mangakas:
    m.start()
for c in cuerposf:
    c.start()
for e in ensambladores:
    e.start()
for m in mangakas:
    m.join()
for c in cuerposf:
    c.join()
for e in ensambladores:
    e.join()
