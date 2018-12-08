#En una fabrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del numero de computadoras que compre. Si las computadoras son menos de 5, se les
#dará un 10% de descuento sobre el total de la compra; si el numero de computadoras es mayor o igual a cinco, pero al menos 10 se le otorga un 20% de descuento; y si son 10
#o más se les da un 40% de descuento. El precio de cada computadora es de $11,000

#ANALISIS DE SITUACION
#cantidad_computadoras < 5 -->>> descuento = 10%
#cantidad_computadoras => 5 y cantidad_computadoras =< 10 -->>> descuento = 20%
#cantidad_computadoras > 10 -->>> descuento = 40%

print("Por favor ingresar cantidad de computadoras a comprar: ")
cantidad_computadoras = int(input())

if cantidad_computadoras < 5:
    valor_compra = (cantidad_computadoras * 11000)*0.9
    print("El valor de su compra es $" + str(valor_compra) + " pesos, el cual incluye un descuento de 10%")

elif cantidad_computadoras >= 5 and cantidad_computadoras <= 10:
    valor_compra = (cantidad_computadoras * 11000)*0.8
    print("El valor de su compra es $" + str(valor_compra) + " pesos, el cual incluye un descuento de 20%")
    
if cantidad_computadoras > 10:
    valor_compra = (cantidad_computadoras * 11000)*0.6
    print("El valor de su compra es $" + str(valor_compra) + " pesos, el cual incluye un descuento de 40%")
    
