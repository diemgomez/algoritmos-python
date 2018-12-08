#Calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es $800 si se compra menos de 5 llantas y $700 si se compra 5 o más.

print("Ingresar cantidad de llantas a comprar:")
cantidad_llantas = int(input())

if cantidad_llantas < 5:
    precio_total = cantidad_llantas * 800
    print("El precio total de su compra es:" + str(precio_total))
    print("El costo unitario de cada llanta es de $800 pesos.")
    
elif cantidad_llantas > 5:
    precio_total = cantidad_llantas * 700
    print("El precio total de su compra es:" + str(precio_total))
    print("El costo unitario de cada llanta es de $700 pesos.")