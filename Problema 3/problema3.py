class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.pila = None

    def push(self, v):
        nuevo = Nodo(v)
        nuevo.siguiente = self.pila
        self.pila = nuevo

    def pop(self):
        if not self.pila:
            print("La pila está vacía")
            return None

        nodo = self.pila
        self.pila = nodo.siguiente
        v = nodo.valor
        print("Se borró el nodo", v)
        return v

    def mostrar_pila(self, pila):
        if not pila:
            print("La pila está vacia")
            return None

        if not pila.siguiente:
            print(pila.valor)
        else:
            print(pila.valor, end=' ')
            self.mostrar_pila(pila.siguiente)

def main():
    pila = Pila()
    pila.push(20)
    pila.push(10)
    pila.mostrar_pila(pila.pila)
    pila.pop()
    pila.push(40)
    pila.push(30)
    pila.mostrar_pila(pila.pila)

    pila.pop()
    pila.pop()
    pila.push(90)
    pila.pop()
    pila.pop()
    pila.mostrar_pila(pila.pila)

if __name__ == '__main__':
    main()