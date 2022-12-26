print("El alumno procedera a poner 4 notas, el programa arrojara si aprobó o desaprobó")
numero1 = float(input("Coloque la nota 1...... "))
while numero1<0 or numero1>20:
    print("NOTA NO VALIDA")
    numero1 = float(input("Coloque la nota 1...... "))
numero2 = float(input("Coloque la nota 2...... "))
while numero2<0 or numero2>20:
    print("NOTA NO VALIDA")
    numero2 = float(input("Coloque la nota 2...... "))
numero3 = float(input("Coloque la nota 3...... "))
while numero3<0 or numero3>20:
    print("NOTA NO VALIDA")
    numero3 = float(input("Coloque la nota 3...... "))
numero4 = float(input("Coloque la nota de 4...... "))
while numero4<0 or numero4>20:
    print("NOTA NO VALIDA")
    numero4 = float(input("Coloque la nota de 4...... "))

PROMEDIO = (numero1+numero2+numero3+numero4)/4
print("Su promedio final es: ",PROMEDIO )
