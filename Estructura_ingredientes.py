from msilib.schema import Class


class Nodo:
   def __init__(self, objeto_ingrediente):
        self.objeto_ingrediente = objeto_ingrediente
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

    
    def añadirNodo(self, objeto_ing):
        nuevoNodo = Nodo(objeto_ing)

        #insertamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo

        #si por lo menos hay un nodo, insertamos al final
        else:
            print("Insertando nodo al final")
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo


    def imprimirLista(self):
        print("INGREDIENTES: ")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo:"+str(contador)+" -> "+nodoTemporal.objeto_ingrediente.ingrediente+" TIEMPO: --> "+str(nodoTemporal.objeto_ingrediente.tiempo))
            nodoTemporal = nodoTemporal.siguiente


    def borrarNodo(self, dato):
        #creamos un nodo temporal
        nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.head

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:

            #validamos si ese nodo es el que busco
            if nodoTemporal.dato == dato:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.head:
                    print("Borrando dato en la cabeza")
                    self.head = self.head.siguiente
                    nodoTemporal.siguiente = None
                    self.head.anterior = None
                #Si ese nodo es la cola
                elif nodoTemporal == self.end:
                    print("Borrando dato en la cola")
                    self.end = self.end.anterior
                    nodoTemporal.anterior = None
                    self.end.siguiente = None
                #Si no es ni la cola ni la cabeza
                else:
                    print("Borrando dato del medio")
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None

            nodoTemporal = nodoTemporal.siguiente


