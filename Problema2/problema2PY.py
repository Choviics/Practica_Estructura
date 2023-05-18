class Nodo:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

raiz = None

def insertar(x):
    global raiz
    nuevo = Nodo(x)
    if raiz is None:
        raiz = nuevo
    else:
        anterior = None
        reco = raiz
        while reco is not None:
            anterior = reco
            if x < reco.info:
                reco = reco.izq
            else:
                reco = reco.der
        if x < anterior.info:
            anterior.izq = nuevo
        else:
            anterior.der = nuevo


def imprimirPre(reco):
    if reco is not None:
        print(reco.info, end="-")
        imprimirPre(reco.izq)
        imprimirPre(reco.der)


def imprimirEntre(reco):
    if reco is not None:
        imprimirEntre(reco.izq)
        print(reco.info, end="-")
        imprimirEntre(reco.der)


def imprimirPost(reco):
    if reco is not None:
        imprimirPost(reco.izq)
        imprimirPost(reco.der)
        print(reco.info, end="-")


def borrar(reco):
    if reco is not None:
        borrar(reco.izq)
        borrar(reco.der)
        del reco


insertar(50)
insertar(25)
insertar(70)
insertar(8)
insertar(30)
print("Impresion preorden: ", end="")
imprimirPre(raiz)
print("\n\n")
print("Impresion entreorden: ", end="")
imprimirEntre(raiz)
print("\n\n")
print("Impresion postorden: ", end="")
imprimirPost(raiz)
borrar(raiz)