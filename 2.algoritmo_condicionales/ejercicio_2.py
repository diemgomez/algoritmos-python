#En una llantera se ha establecido una promocion de las llantas marca "Ponchadas", dicha promocion consiste en lo siguiente:
#a.Si se compran menos de cinco llantas el precio es de $300 cada una, de $250 si se compran de cinco a 10 y de $200 si se compran más de 10.

#Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compra y la que tiene que pagar por el total de la compra.
print("Bienvenido al almacen ZEMOG")
print("Por favor ingresar la cantidad de llantas a comprar:")
cantidad_llantas = int(input())
if cantidad_llantas < 5:
    valor_total = cantidad_llantas * 300
    print("Por su compra, el costo de cada llanta es 300 pesos")
    print("El valor total de su compra es:", str(valor_total), "pesos.")

elif cantidad_llantas >= 5 and cantidad_llantas <= 10:
    valor_total = cantidad_llantas * 250
    print("Por su compra, el costo de cada llanta es 250 pesos")
    print("El valor total de su compra es:", str(valor_total), "pesos.")

else:
    valor_total = cantidad_llantas * 200
    print("Por su compra, el costo de cada llanta es 200 pesos")
    print("El valor total de su compra es:", str(valor_total), "pesos.")