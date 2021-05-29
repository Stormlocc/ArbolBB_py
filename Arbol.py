from Persona import *
# Clase arbol
class Arbol():

    # Constructores de Nodo
    def __init__(self) -> None:
        self.dato = None
        self.subArbolDerecho = None
        self.subArbolIzquierdo = None

    # Metodos Adicionales
    def EstaVacio(self):
        return self.dato == None

    def Agregar(self, dato):
        if(self.EstaVacio()):
            self.dato = dato
        else:
            # Determinar en que direccion se agrega
            if(self.dato.get_dni() < dato.get_dni()):
                # Agregar en la derecha
                if(self.subArbolDerecho == None):
                    self.subArbolDerecho = Arbol()
                    self.subArbolDerecho.Agregar(dato)
                else:
                    self.subArbolDerecho.Agregar(dato)
            else:
                # Agregar en la izquierda
                if(self.subArbolIzquierdo == None):
                    self.subArbolIzquierdo = Arbol()
                    self.subArbolIzquierdo.Agregar(dato)
                else:
                    self.subArbolIzquierdo.Agregar(dato)

    def PreOrden(self):  # Raiz - Izq - Der
        if(not(self.EstaVacio())):
            print(self.dato)
        if(self.subArbolIzquierdo != None):
            self.subArbolIzquierdo.PreOrden()
        if(self.subArbolDerecho != None):
            self.subArbolDerecho.PreOrden()
