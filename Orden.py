from Ingrediente import *


class Orden:
    def __init__(self, id_orden, nombre_cliente, dpi_cliente, cant_pizzas, lista_ingred, tiempo_total):
        self.id_orden = id_orden
        self.nombre_cliente = nombre_cliente
        self.dpi_cliente = dpi_cliente
        self.cant_pizzas = cant_pizzas
        self.lista_ingred = lista_ingred
        self.tiempo_total = tiempo_total
        


    def mostrar_orden(self):
        print("NOMBRE:  "+str(self.nombre)+" FILAS: "+str(self.filas)+" COLUMNAS: "+str(self.columas)+" PRECIO VOLTEO: "+str(self.volteo)+" PRECIO INTERCAMBIO: "+str(self.intercambio)+"")
        for patron in self.patrones: 
            patron.mostrar_patron()
