#Una fruteria ofrece las manzanas con descuento segun la siguiente tabla:
#CANTIDAD KILOS COMPRADOS             %DESCUENTO
#        0 - 2                            0%
#      2.01 - 5                           10%
#      5.01 - 10                          15%
#     10.01 en adelante                   20%

print("Por favor ingresar cantidad kilos de manzanas a comprar:")
cantidad_manzanas = int(input())

print("Por favor ingresar valor unitario del kilo:")
precio = float(input())

if cantidad_manzanas <= 2:
    valor_total = cantidad_manzanas * precio
    print("El valor total de su compra es", str(valor_total), "pesos. No tiene descuento.")
    
elif cantidad_manzanas > 2 and cantidad_manzanas <= 5:
    valor_total = (cantidad_manzanas * precio)*0.9
    print("El valor total de su compra es", str(valor_total), "pesos. Tiene un 10% de descuento.")

elif cantidad_manzanas > 5 and cantidad_manzanas <= 10:
    valor_total = (cantidad_manzanas * precio)*0.85
    print("El valor total de su compra es", str(valor_total), "pesos. Tiene un 15% de descuento.")

else:
    valor_total = (cantidad_manzanas * precio)*0.8
    print("El valor total de su compra es", str(valor_total), "pesos. Tiene un 20% de descuento.")