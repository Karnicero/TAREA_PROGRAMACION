# # Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 
# # 55% del promedio de sus tres calificaciones parciales.
# 
# #       30% de la calificación del examen final.
# 
# #       15% de la calificación de un trabajo final.

a=float(input("ingrese la primer nota del parcial"))
b=float(input("ingrese la segunda nota del parcial"))
c=float(input("ingrese la tercera del parcial"))
d=float(input("ingrese la nota del examen final"))
e=float(input("ingrese la nota del trabajo final"))

G=((a+b+c)/3)*0.55

H= d*0.30

I= e*0.15

K= G+H+I


print("la calificación final del alumno es:" , K)

