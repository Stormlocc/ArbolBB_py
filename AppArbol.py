from Arbol import *
from Persona import * 
from Alumno import *
from Docente import *
#from = carpeta o archivo 
#import = modulos a usar
#https://www.youtube.com/watch?v=Zf9sN-w0BVE paquetes para incluir clases o/y function

#<<<<<<<<<<<< Programa principal >>>>>>>>>>>>>>>>>>>>>>
#Instanciamos el arbol
arbolito = Arbol()

#Agregamos personas
p1 = Persona()
p1.Leer()
arbolito.Agregar(p1)

p2 = Persona()
p2.Leer()
arbolito.Agregar(p2)

p3 = Persona()
p3.Leer()
arbolito.Agregar(p3)

p4 = Persona()
p4.Leer()
arbolito.Agregar(p4)

p5 = Persona()
p5.Leer()
arbolito.Agregar(p5)

p6 = Persona()
p6.Leer()
arbolito.Agregar(p6)

p7 = Persona()
p7.Leer()
arbolito.Agregar(p7)


arbolito.PreOrden()
