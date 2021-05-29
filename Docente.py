#hereda de Persona
from Persona import *

class Docente(Persona):
    pass

    def __init__(self):
        super().__init__()
        self.__asignatura = None

    def Leer(self):
        super().Leer()
        self.__asignatura = str(input("Ingres Asignatura: "))
        
    def __str__(self):
        return super().__str__() + " , " + str(self.__asignatura)


