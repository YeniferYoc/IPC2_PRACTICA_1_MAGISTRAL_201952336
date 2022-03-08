import Estructura_cola

listaDoble = Estructura_cola.ListaDoble()
listaDoble.añadirNodoPrincipio("Fresa")
listaDoble.añadirNodoPrincipio("Vainilla")
listaDoble.añadirNodoPrincipio("Chocolate")
listaDoble.añadirNodoPrincipio("Pistacho")

#listaDoble2 = Estructuras.ListaDoble()
#listaDoble2.añadirNodoFinal
#listaDoble2.añadirNodoFinal("Chocolate")
#listaDoble2.añadirNodoFinal("Pistacho")

if __name__ == '__main__':
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    listaDoble.borrarNodo("Vainilla")
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    #y cualquier otra instrucción