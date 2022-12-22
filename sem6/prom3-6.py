#programa que pide una nota de un examen(del 1 al 105) por teclado y muestra la nota como "Sobresaliente", "Notable", "Bien", "Suficiente", "Suspendido". 

#Multiples

a=float(input("ingrese la nota del examen"))
if a >=1 and a <= 4:
    print("Suspenso")
elif a == 5:
    print("Suficiente")
elif a == 6 or a == 7:
	print("Bien")
elif a == 8:
	print("Notable")
elif a ==9 or a == 10:
	print("Sobresaliente")
else:
	print("Nota incorrecta")

#elif: se usa cuando la primera declaración if no es verdadera, pero desea verificar otra condición. Es decir, si las declaraciones se emparejan con 
# las declaraciones elif y else para realizar una serie de comprobaciones.

#expreciones logicas
# #  ==,= igual que           >mayor que          <menor que          >=mayor o igual que          <=menor o igual que







