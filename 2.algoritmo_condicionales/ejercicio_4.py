#Un proveedor de estereos ofrece un descuento de 10% sobre el precio sin IVA, de algun aparato si esta cuesta $2000 o más, Además, independientemente de esto, ofrece un 5%
#de descuento si la marca es "NOSY". Determinar cuanto pagará, con IVA incluido, un cliente cualquiera por la compra de su aparato.

print("Ingresar el nombre de la marca")
nombre_marca = str(input())

print("Ingresar el valor del articulo")
valor_producto = float(input())

if nombre_marca == "NOSY" and valor_producto >= 2000:
    descuento = valor_producto * 0.15
    valor_total = (valor_producto - descuento)*1.19
    print("El valor total de su compra es", str(valor_total), "pesos. En el cual incluye un 10% por el valor de su compra y un 5% por comprar un producto marca NOSY.")

elif valor_producto >= 2000:
    descuento = valor_producto * 0.10
    valor_total = (valor_producto - descuento)*1.19
    print("El valor total de su compra es", str(valor_total), "pesos. En el cual incluye un 10% por el valor de su compra")

elif valor_producto < 2000 and nombre_marca == "NOSY":
    descuento = valor_producto * 0.05
    valor_total = (valor_producto - descuento)*1.19
    print("El valor total de su compra es", str(valor_total), "pesos. En el cual incluye un 5% de decuento por la compra un producto marca NOSY.")
    
else:
    valor_total = (valor_producto)*1.19
    print("El valor total de su compra es", str(valor_total), "pesos.")
    
    
    

