import threading, time, random

locke = threading.Lock()
lockl = threading.Lock()
item = []


def Escritorhilo(aidi,locke,lockl):
    global item
    global sl

    # if not escrito
    while True:
        if not locke.locked():
            # x = True
            # escrito = True
            locke.acquire()

            print("Soy el escritor: " + str(aidi) + " usando la BD")
            item = [random.randint(0, 100), aidi]
            print("Soy el escritor: " + str(aidi) + " dejando de usar la BD")
            locke.release()
            # x = False
            break
        else:
            time.sleep(sl)


def Lector(aidi,locke,lockl):
    global sl
    global item

    while True:
        if not lockl.locked():
            locke.acquire()
            #lockl.acquire()
            print("Soy el lector: " + str(aidi) + " usando la BD")
            time.sleep(sl)
            print("Soy el lector: " + str(aidi) + " el escritor:" + str(item[1]) + " escribio: " + str(item[0]))
            print("Soy el lector: " + str(aidi) + " dejando de usar la BD")
            locke.release()
            #lockl.release()
            break
        else:
            time.sleep(sl)
            print("El lector: " + str(aidi) + " intento usar la BD")


# n = input("ingresa el numero de hilos")
sl = int(input("ingresa el tiempo de espera en segundos"))
# NUM_THREADS = int(n)
nescritores = int(str(input("Ingrese el numero de escritores")))
nlectores = int(str(input("Ingrese el numero de escritores")))


barrier = threading.Barrier(nescritores)

Escritors = [threading.Thread(name='worker-%s' % i, target=Escritorhilo, args=(barrier,locke,lockl), )
             for i in range(nescritores)]
Lectors = [threading.Thread(name='worker-%s' % i, target=Lector, args=(barrier,locke,lockl), )
           for i in range(nlectores)]
# for y in range(0,int(n)):
# Escritor=threading.Thread(target=Escritorhilo,args=(y,))
# Escritor.start()
# print("escritor ini")
# lector=threading.Thread(target=Lector,args=(y,))
# lector.start()

for t in Escritors:
    t.start()

for t in Lectors:
    t.start()

for t in Escritors:
    t.join()
for t in Lectors:
    t.join()
