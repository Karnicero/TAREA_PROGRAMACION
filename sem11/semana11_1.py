"""
Diseña un algoritmo en el que se ingrese 2 digitos para sumarlos
 y repetir el ciclo usando el while.
"""
#declaracion de variables
total = 0 

#entrada
#proceso
#salida
rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer digito: "))
    num2 = int (input ("ingrese el segundo digito: "))
    total = total + num1 + num2
    print ("La suma es: ", total)
    rpt = str (input ("Desea realizar otra suma? si/no : "))
