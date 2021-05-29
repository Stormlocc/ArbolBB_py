# Clase heredera de ancestro
from Persona import *

class Alumno(Persona):
    pass

    def __init__(self):
        super().__init__()
        self.__escuela = None

    def Leer(self):
        super().Leer()
        self.__escuela = str(input("Ingrese Escuela: "))

    def __str__(self):
        return super().__str__() + " , "+str(self.__escuela)
