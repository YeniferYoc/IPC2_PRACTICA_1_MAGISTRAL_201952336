from sre_constants import OP_IGNORE
import Estructura_cola
import Estructura_ingredientes
from Ingrediente import *
from Orden import *
from graphviz import Graph
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from os import startfile
from os import system

lista_ordenes = Estructura_cola.ListaDoble()



def menu():
    salir = False
    contador_ordenes_ = 0
  
    while salir != True:    
        #AQUI ESTA EL MENU PRINCIPAL    
        print("")
        print("--------------------------------------------------------------------")
        print("1. AGREGAR ORDEN")
        print("2. VER ORDENES EN COLA")
        print("3. DESPACHAR ORDEN")
        print("4. ELIMINAR ORDEN")
        print("5. MODIFICAR ORDEN")
        print("6. VER DATOS DEL ESTUDIANTE")
        print("7. SALIR")
        print("--------------------------------------------------------------------")
        print("")
        opcion = int(input("DIGITE EL NUMERO DE LA OPCION CORRESPONDIENTE "))

        if(opcion ==1):
            print("")
            print("AGREGAR NUEVA ORDEN ")
            contador_ordenes_ += 1
            id_orden = contador_ordenes_
            nombre_cliente = input("NOMBRE DEL CLIENTE: ")
            dpi_cliente = input("DPI CLIENTE: ")
            cant_pizzas = int(input("CANTIDAD DE PIZZAS: "))
            cant_ingred = int(input("¿CUANTOS INGREDIENTES DESEA AGREGAR A SUS PIZZAS?: "))
            tiempo_total = 0
            print("INGREDIENTES: ")
            lista_ingredientes = Estructura_ingredientes.ListaDoble()
            contador_ing = 0
            for i in range(cant_ingred):
                contador_ing +=  1
                nombre_ing = ""
                tiempo_ing = ""
                print("")
                print("1.PEPERONI")
                print("2.SALCHICHA")
                print("3.CARNE")
                print("4. QUESO")
                print("5: PIÑA")
                print("")
                op_ing = int(input("INGRESE EL NUMERO DEL INGREDIENTE QUE DESEE AGREGAR: "))
                if op_ing == 1:
                    nombre_ing = "Peperoni"
                    tiempo_ing = 3
                if op_ing == 2 :
                    nombre_ing = "Salchicha"
                    tiempo_ing = 4
                if op_ing == 3:
                    nombre_ing = "Carne"
                    tiempo_ing = 10
                if op_ing == 4 :
                    nombre_ing = "Queso"
                    tiempo_ing = 5
                if op_ing == 5:
                    nombre_ing = "Piña"
                    tiempo_ing = 2
                ingred_nuevo = Ingrediente(nombre_ing,tiempo_ing)
                lista_ingredientes.añadirNodo(ingred_nuevo)
                tiempo_total += tiempo_ing
            
            orden_nueva = Orden(id_orden, nombre_cliente, dpi_cliente, cant_pizzas,lista_ingredientes,tiempo_total)
            lista_ordenes.añadirNodo(orden_nueva)
            print("ORDEN AGREGADA CON EXITO, DEBE ESPERAR: "+str(tiempo_total)+" mins. ")
            print("")
                
        if (opcion == 2):
            print("MOSTRAR ORDENES: ")
            lista_ordenes.imprimirLista()



            mi_archivo= open('ordenes_cola.dot','w')
            mi_archivo.write("graph L{")
            mi_archivo.write("node[shape = box fillcolor = \"#FFEDBB\" style  = filled]")
            mi_archivo.write("subgraph cluster_p{")
            mi_archivo.write("label= \"COLA DE ORDENES\"")
            mi_archivo.write("bgcolor = \"#398D9C\"")
            mi_archivo.write("edge [dir = \"both\"]")
            celda="orden"
            contador = 1 
            mensaje =''
            nodoTemporal = Estructura_cola.Nodo("")

            nodoTemporal = lista_ordenes.head
            contador = 1
            while nodoTemporal != None:
            
                mensaje =str(celda+str(contador))
                    
                mi_archivo.write(mensaje+"[label= \""+str(nodoTemporal.objeto_orden.id_orden)+"\", fillcolor =\"cyan\", group = 2 ];")
                contador += 1 
                nodoTemporal = nodoTemporal.siguiente
            '''
            contador2 = 1
            for j in range(contador-1):
                mensaje =str(celda+str(contador2))
                sig_ = str(celda+str(contador2+1))
                mi_archivo.write(mensaje+"->"+sig_+";")
                contador2 +=1
            
            contador_same = 1
            mi_archivo.write("{rank = same;")
                
            for j in range(contador-1):
                mensaje =str(celda+str(contador_same))
                mi_archivo.write(mensaje+";")
                contador_same+=1

                mi_archivo.write("}")

            '''

            
            mi_archivo.write("}")
            mi_archivo.write("}")

            mi_archivo.close()

            system('dot -Tpng ordenes_cola.dot -o ordenes_cola.png')
            system('cd./ordenes_cola.png')
            startfile('ordenes_cola.png')
        
        if (opcion == 3):
            print("DESPAHANDO LA PRIMER ORDEN DE LA COLA ")
            nodo_temporal = Estructura_cola.Nodo("")
            nodo_temporal = lista_ordenes.head
            print("*********************************************************************")
            print("")
            print(" ID ORDEN: "+str(nodo_temporal.objeto_orden.id_orden))
            print("Nombre Cliente: "+nodo_temporal.objeto_orden.nombre_cliente+ " Dpi cliente: "+str(nodo_temporal.objeto_orden.dpi_cliente))
            print("Cantida de pizzas:"+str(nodo_temporal.objeto_orden.cant_pizzas))
            nodo_temporal.objeto_orden.lista_ingred.imprimirLista()
            print("")
            print("*********************************************************************")
            lista_ordenes.borrarCola()
            lista_ordenes.imprimirLista()

        if opcion == 4:
            id_buscar_eliminar = int(input("INGRESE EL NUMERO DE ORDEN QUE DESEA ELIMINAR: "))
            lista_ordenes.borrarNodo(id_buscar_eliminar)

        if opcion == 5:
            id_buscar_mod = int(input("INGRESE EL NUMERO DE ORDEN QUE DESEA MODIFICAR: "))
            lista_ordenes.Modificar(id_buscar_mod)

        if opcion == 6:
            print("########################## DATOS DEL ESTUDIANTE ##########################")
            print("NOMBRE: YENIFER ESTER YOC LARIOS")
            print("CARNE: 201952336")
            print("##########################################################################")

        if opcion == 7:
            salir = True
            print("ADIOS!!!!!!!!!!! :)")

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  