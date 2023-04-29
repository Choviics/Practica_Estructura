class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.prev = None
        self.next = None
        self.up = None
        self.down1 = None
        self.down2 = None
        
class lista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ini = None
        self.final = None
        
def crearL(nombre):
    List = lista(nombre)
    List.ini = List.final = None
    return List

def creanodo(nombre):
    aux = Nodo(nombre)
    aux.prev = aux.next = aux.up = aux.down1 = aux.down2 = None
    return aux

def listaenlazada1():
    c1 = crearL("lista de cargos")
    gerente = creanodo("Gerente")
    jefedeproyecto = creanodo("jefe de Proyecto")
    programador = creanodo("Programador")
    gerente.next = jefedeproyecto
    jefedeproyecto.prev = gerente
    jefedeproyecto.next = programador
    programador.prev = jefedeproyecto
    c1.ini = gerente
    c1.final = programador
    return c1

def listaenlazada2(c1):
    c2 = crearL("Lista de roles")
    analista = creanodo("Analista")
    admin = creanodo("Administrador")
    auditor = creanodo("Auditor")
    prod = creanodo("Produccion")
    c1.ini.down1 = analista
    analista.up = c1.ini
    analista.next = admin
    c1.ini.down2 = admin
    admin.up = c1.ini
    admin.next = auditor
    admin.prev = analista
    c1.ini.next.down1 = auditor
    auditor.up = c1.ini.next
    auditor.next = prod
    auditor.prev = admin
    c1.final.down1 = prod
    prod.up = c1.final
    prod.prev = auditor
    c2.ini = analista
    c2.final = prod
    return c2

def listaenlazada3(c2):
    c3 = crearL("Lista de Permisos")
    edicion = creanodo("Edicion de Archivos Gerenciales")
    progreso = creanodo("Administracion de Progreso")
    procesos = creanodo("Verificador de Procesos")
    empresa = creanodo("Edicion de programas empresariales")
    c2.ini.down1 = edicion
    edicion.up = c2.ini
    edicion.next = progreso
    c2.ini.next.down1 = progreso
    progreso.next = procesos
    progreso.prev = edicion
    progreso.up = c2.ini.next
    c2.final.prev.down1 = procesos
    procesos.up = c2.final.prev
    procesos.next = empresa
    procesos.prev = progreso
    c2.final.down1 = empresa
    empresa.up = c2.final
    empresa.prev = procesos
    c3.ini = edicion
    c3.final = empresa
    return c3

def listaenlazada4(c3):
    c4 = crearL("Lista de personal")
    raul = creanodo("Raul Alvarez")
    ibai = creanodo("Ibai Llanos")
    ruben = creanodo("Ruben Doblas")
    guillermo = creanodo("Guillermo Diaz")
    joaquin = creanodo("Joaquin Dominguez")
    juan = creanodo("Juan Guarnizo")
    c3.ini.down1 = raul
    raul.next = ibai
    raul.up = c3.ini
    c3.ini.next.down1 = ibai
    ibai.prev = raul
    ibai.next = ruben
    ibai.up = c3.ini.next
    c3.ini.next.down2 = ruben
    ruben.up = c3.ini.next
    ruben.prev = ibai
    ruben.next = guillermo
    c3.final.prev.down1 = guillermo
    guillermo.up = c3.final.prev
    guillermo.prev = ruben
    guillermo.next = joaquin
    c3.final.down1 = joaquin
    joaquin.up = c3.final
    joaquin.prev = guillermo
    joaquin.next = juan
    c3.final.down2 = juan
    juan.up = c3.final
    juan.prev = joaquin
    c4.ini = raul
    c4.final = juan
    return c4

def busqueda(c1,c2,c3,c4, nombre):
    aux = c1.ini
    if(aux.valor != nombre):
        aux = encontrar(aux, nombre)
        if(aux.valor != nombre):
            aux = c2.ini
            aux = encontrar(aux, nombre)
            if(aux.valor != nombre):
                aux = c3.ini
                aux = encontrar(aux, nombre)
                if(aux.valor != nombre):
                    aux = c4.ini
                    aux = encontrar(aux, nombre)
    return aux


def encontrar(nodo, nombre):
    aux = nodo
    while(aux.next != None):
        if aux.valor == nombre:
            return aux
        else:
            aux = aux.next
            if aux.valor == nombre:
                return aux
    return nodo

def Mostrar_derecha(nodo):
    aux = nodo
    if(nodo.down2 != None):
        aux = aux.down2
        print("{}".format(aux.valor))
        while(aux.down1 != None):
            if(aux.down2 != None):
                Mostrar_derecha(aux)
            aux = aux.down1
            print("{}".format(aux.valor))

def Mostrar_izquierda(nodo):
    aux = nodo
    if(nodo.down1 != None):
        aux = aux.down1
        print("{}".format(aux.valor))
        while(aux.down1 != None):
            if(aux.down2 != None):
                Mostrar_derecha(aux)
            aux = aux.down1
            print("{}".format(aux.valor))

def Mostrar_arriba(nodo):
    aux = nodo
    if nodo.up != None:
        while aux.up != None:
            aux = aux.up
            print("{}".format(aux.valor))
        
def mostrarnodos(principal):
    aux = principal
    Mostrar_arriba(aux)
    Mostrar_izquierda(aux)
    Mostrar_derecha(aux)

def main():
    c1 = listaenlazada1()
    c2 = listaenlazada2(c1)
    c3 = listaenlazada3(c2)
    c4 = listaenlazada4(c3)
    nombre = input("Escriba el nombre de un nodo: ")
    main_node = busqueda(c1, c2, c3, c4, nombre)
    mostrarnodos(main_node)

if __name__ == '__main__':
    main()