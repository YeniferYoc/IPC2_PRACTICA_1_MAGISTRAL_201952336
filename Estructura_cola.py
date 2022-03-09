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
            
            nodoTemporal = nodoTemporal.siguiente

        print("----------------------- LISTA TERMINADA --------------------------------")

    def borrarCola(self):
        #creamos un nodo temporal
        nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.head
        self.head = self.head.siguiente

    def borrarNodo(self, id):
            #creamos un nodo temporal
            nodoTemporal = Nodo("")

            #el temporal empieza en la cabeza
            nodoTemporal = self.head

            #Mientras que el temporal no sea nulo
            while nodoTemporal != None:

                #validamos si ese nodo es el que busco
                if nodoTemporal.objeto_orden.id_orden == id:
                    print("--------------------------------------------------------------------")
                    print("")
                    print("ID ORDEN: "+str(nodoTemporal.objeto_orden.id_orden))
                    print("Nombre Cliente: "+nodoTemporal.objeto_orden.nombre_cliente+ " Dpi cliente: "+str(nodoTemporal.objeto_orden.dpi_cliente))
                    print("Cantida de pizzas:"+str(nodoTemporal.objeto_orden.cant_pizzas))
                    nodoTemporal.objeto_orden.lista_ingred.imprimirLista()
                    print("")
                    print("---------------------------------------------------------------------")
                    #Si ese nodo es la cabeza
                    if nodoTemporal == self.head:

                        self.head = self.head.siguiente
                        nodoTemporal.siguiente = None
                        self.head.anterior = None
                    #Si ese nodo es la cola
                    elif nodoTemporal == self.end:
                        
                        self.end = self.end.anterior
                        nodoTemporal.anterior = None
                        self.end.siguiente = None
                    #Si no es ni la cola ni la cabeza
                    else:
                        
                        nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                        nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                        nodoTemporal.siguiente = nodoTemporal.anterior = None

                nodoTemporal = nodoTemporal.siguiente

    def Modificar(self, id):
                #creamos un nodo temporal
                nodoTemporal = Nodo("")

                #el temporal empieza en la cabeza
                nodoTemporal = self.head

                #Mientras que el temporal no sea nulo
                while nodoTemporal != None:

                    #validamos si ese nodo es el que busco
                    if nodoTemporal.objeto_orden.id_orden == id:
                        print("--------------------------------------------------------------------")
                        print("")
                        print("ID ORDEN: "+str(nodoTemporal.objeto_orden.id_orden))
                        print("1. Nombre Cliente: "+nodoTemporal.objeto_orden.nombre_cliente)
                        print("2. Dpi cliente: "+str(nodoTemporal.objeto_orden.dpi_cliente))
                        print("3. Cantida de pizzas:"+str(nodoTemporal.objeto_orden.cant_pizzas))
                        nodoTemporal.objeto_orden.lista_ingred.imprimirLista()
                        print("")
                        print("---------------------------------------------------------------------")
                        mod = int(input("QUE DESEA MODIFICAR? "))
                        if mod == 1:
                            nodoTemporal.objeto_orden.nombre_cliente = input("INGRESE EL NUEVO NOMBRE ")
                        if mod == 2:
                            nodoTemporal.objeto_orden.dpi_cliente = input("INGRESE EL NUEVO DPI ")
                        if mod == 3:
                            nodoTemporal.objeto_orden.cant_pizzas = input("INGRESE LA CANTIDAD DE PIZZAS ")
                        print("")

                    nodoTemporal = nodoTemporal.siguiente
