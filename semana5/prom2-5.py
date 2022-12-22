#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones 
#por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

y=float(input("ingrese su sueldo base"))
r=float(input("ingresar el valor de la venta 1" ))
a=float(input("ingresar el valor de la venta 2" ))
b=float(input("ingresar el valor de la venta 3" ))

c=(r*0.10)+(a*0.10)+(b*0.10)
d= c+y

print("el valor total de las 3 comisiones de la venta del mes es:" , c)
print("el valor total que gano en el mes mas las comisiones es:" , d)