"""
Diseña un algoritmo en el que se ingrese 2 digitos para sumarlos
 y los acumule usando el while.
"""
#declaracion de variables
acu = 0 
cont = 0

#entrada
#proceso
#salida
rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer digito: "))
    num2 = int (input ("ingrese el segundo digito: "))
    acu = acu + num1 + num2
    print ("La suma es: ", acu)
    print("La acumulación de suma es de: " , acu)
    
    rpt = str (input ("Desea realizar otra suma? si/no : "))
