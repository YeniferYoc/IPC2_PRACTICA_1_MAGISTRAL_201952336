class Ingrediente:
    def __init__(self, ingrediente, tiempo):
        self.ingrediente = ingrediente
        self.tiempo = tiempo

    def mostrar_ingrediente(self):
        print("INGREDIENTE: "+str(self.ingrediente)+" TIEMPO: "+str(self.tiempo))