from Arbol import *
#from = carpeta o archivo 
#import = modulos a usar
#https://www.youtube.com/watch?v=Zf9sN-w0BVE paquetes para incluir clases o/y function

#<<<<<<<<<<<< Programa principal >>>>>>>>>>>>>>>>>>>>>>

#Instanciamos el arbol
arbolito = Arbol()
#Agregamos el primer dato
arbolito.AgregarDato("l")
arbolito.AgregarDato("m")
arbolito.AgregarDato("h")
arbolito.AgregarDato("n")
arbolito.AgregarDato("o")
arbolito.AgregarDato("b")
arbolito.AgregarDato("z")

#Mostramos en PreOrden los datos
arbolito.PreOrden()

print("Termino programa version #1.0")
