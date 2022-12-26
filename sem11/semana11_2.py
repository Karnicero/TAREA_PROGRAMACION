"""
Diseña un algoritmo en el que se ingrese 2 digitos para restarlos
y el programa los contabilice usando el while.
"""
#declaracion de variables
cont = 0
resta = 0
#entrada
#proceso
#salida
rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer digito: "))
    num2 = int (input ("ingrese el segundo digito: "))
    cont = cont + 2
    resta = num1 - num2
    print ("La resta es: ", resta)
    print("Contador de cuantos digitos ingresó: ", cont)

    rpt = str (input ("¿Desea realizar otra resta? si/no : "))
