#Un vendedor recibe un sueldo base mas un 10% extra por comision de sus ventas, el vendedor desea saber cuanto dinero obtendra por concepto de
#comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
print("Bienvenidos a la plataforma de vendedores")
print('A continuacion ingresar el sueldo base:')
sueldo_base = float(input())
print('Por favor ingresar la cantidad de ventas realizadas:')
cantidad_ventas = int(input())

comisiones = (sueldo_base * 0.1)*3

sueldo_neto = sueldo_base + comisiones

print('Señor vendedor, el sueldo devengado es: ', sueldo_neto)
