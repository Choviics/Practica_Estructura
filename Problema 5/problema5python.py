import random

class Node:
    def __init__(self, valor, numero):
        self.numero = numero
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None

def altura(n):
    if n is None:
        return 0
    else:
        return n.altura

def max(a, b):
    return a if a > b else b

def createNode(valor, numero):
    s = Node(valor, numero)
    return s

def obtenerBalance(n):
    if n is None:
        return 0
    else:
        return altura(n.izq) - altura(n.der)

def valorMinimoNodo(n):
    actual = n
    while actual.izq is not None:
        actual = actual.izq
    return actual

def rotacionIzquierda(x):
    y = x.der
    T2 = y.izq
    y.izq = x
    x.der = T2
    x.altura = max(altura(x.izq), altura(x.der)) + 1
    y.altura = max(altura(y.izq), altura(y.der)) + 1
    return y

def rotacionDerecha(y):
    x = y.izq
    T2 = x.der
    x.der = y
    y.izq = T2
    y.altura = max(altura(y.izq), altura(y.der)) + 1
    x.altura = max(altura(x.izq), altura(x.der)) + 1
    return x

def insertarNodo(n, valor, numero):
    if n is None:
        return createNode(valor, numero)
    if valor < n.valor:
        n.izq = insertarNodo(n.izq, valor, numero)
    elif valor > n.valor:
        n.der = insertarNodo(n.der, valor, numero)
    else:
        return n
    
    n.altura = 1 + max(altura(n.izq), altura(n.der))
    fe = obtenerBalance(n)
    
    if fe > 1 and valor < n.izq.valor:
        return rotacionDerecha(n)
    if fe < -1 and valor > n.der.valor:
        return rotacionIzquierda(n)
    if fe > 1 and valor > n.izq.valor:
        n.izq = rotacionIzquierda(n.izq)
        return rotacionDerecha(n)
    if fe < -1 and valor < n.der.valor:
        n.der = rotacionDerecha(n.der)
        return rotacionIzquierda(n)
    
    return n

def inorder(raiz):
    if raiz is not None:
        inorder(raiz.izq)
        print(raiz.valor, end=' ')
        inorder(raiz.der)

def preorder(raiz):
    if raiz is not None:
        print(raiz.valor, end=' ')
        preorder(raiz.izq)
        preorder(raiz.der)

def postorder(raiz):
    if raiz is not None:
        postorder(raiz.izq)
        postorder(raiz.der)
        print(raiz.valor, end=' ')

def buscar(raiz, valor):
    if raiz.valor == valor:
        return raiz.numero
    else:
        if valor > raiz.valor and raiz.der is not None:
            return buscar(raiz.der, valor)
        elif valor < raiz.valor and raiz.izq is not None:
            return buscar(raiz.izq, valor)
    return 0

raiz = None
cantidad = 0

while True:
    print("\n1. Agregar Trabajadores.")
    print("2. Visualizar números identificadores.")
    print("3. Consultar.")
    print("4. Salir\n")
    
    ch = int(input("Elija una opción: "))
    
    if ch == 1:
        random.seed()
        cantidad = int(input("\nIngrese la cantidad de trabajadores a agregar: "))
        for i in range(cantidad):
            valor = random.randint(0, 1000)
            raiz = insertarNodo(raiz, valor, i + 1)
        
    elif ch == 2:
        print("\nRecorrido In order: ")
        inorder(raiz)
        print("\n")
        print("\nRecorrido Pre order: ")
        preorder(raiz)
        print("\n")
        print("\nRecorrido Post order: ")
        postorder(raiz)
        print("\n")
        
    elif ch == 3:
        id = int(input("\nIngrese un número identificador: "))
        print("Trabajador", buscar(raiz, id))
        
    elif ch == 4:
        break

    print(raiz.altura)