class Nodo:
    def __init__(self, objeto_orden):
        self.objeto_orden = objeto_orden
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None


    def añadirNodo(self, objeto_or):
        nuevoNodo = Nodo(objeto_or)

        #insertamos si la lista esta vacia
        if self.head == None:
            self.head = nuevoNodo
            self.end = nuevoNodo

        #si por lo menos hay un nodo, insertamos al final
        else:
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo


    def imprimirLista(self):
        print("------------------------ ORDENES EN COLA --------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("--------------------------------------------------------------------")
            print("")
            print("Nodo:"+str(contador)+" -> ID ORDEN: "+str(nodoTemporal.objeto_orden.id_orden))
            print("Nombre Cliente: "+nodoTemporal.objeto_orden.nombre_cliente+ " Dpi cliente: "+str(nodoTemporal.objeto_orden.dpi_cliente))
            print("Cantida de pizzas:"+str(nodoTemporal.objeto_orden.cant_pizzas))
            nodoTemporal.objeto_orden.lista_ingred.imprimirLista()
            print("")
            print("---------------------------------------------------------------------")
            
            nodoTemporal = nodoTemporal.siguiente

        print("----------------------- LISTA TERMINADA --------------------------------")

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
                    print(nodoTemporal.dato+"xxxxxxx")


            nodoTemporal = nodoTemporal.siguiente