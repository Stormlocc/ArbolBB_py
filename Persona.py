#Clase Ancestro Persona

class Persona():
    def __init__(self):
        self.__nombre= None
        self.__apellido=None
        self.__dni = None
    
    def Crear(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    #Propiedades
    def get_nombre(self):
        return str(self.__nombre)
    def get_apellido(self):
        return str(self.__apellido)
    def get_dni(self):
        return str(self.__dni)

    def Leer(self):
        self.__nombre = str(input("Ingrese nombre: "))
        self.__apellido = str(input("Ingrese apellido: "))
        self.__dni = str(input("Ingrese DNI: ")) 

    def __str__(self):
        return str(self.__nombre) + " , " + str(self.__apellido) + " , " + str(self.__dni)
