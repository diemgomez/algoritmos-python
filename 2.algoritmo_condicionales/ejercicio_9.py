#Lea tres numeros diferentes y determine el numero medio del conjunto de los tres numeros(el numero medio es aquel numero que no es ni mayor, ni menos)

print('Por favor ingresar primer valor: ')
numero_1 = float(input())

print('Por favor ingresar segundo valor: ')
numero_2 = float(input())

print('Por favor ingresar tercer valor: ')
numero_3 = float(input())

if numero_1 > numero_2 and numero_1 > numero_3 and numero_2 > numero_3:

    print("El valor de " + str(numero_2) + " es el de la mitad")
    
elif numero_1 > numero_2 and numero_1 > numero_3 and numero_3 > numero_2:

    print("El valor de " + str(numero_3) + " es el de la mitad")
    
elif numero_3 > numero_1 and numero_3 > numero_2 and numero_2 > numero_1:

    print("El valor de " + str(numero_2) + " es el de la mitad")

elif numero_3 > numero_1 and numero_3 > numero_2 and numero_1 > numero_2:

    print("El valor de " + str(numero_1) + " es el de la mitad")

elif numero_2 > numero_1 and numero_2 > numero_3 and numero_3 > numero_1:

    print("El valor de " + str(numero_3) + " es el de la mitad")

elif numero_2 > numero_1 and numero_2 > numero_3 and numero_1 > numero_3:

    print("El valor de " + str(numero_1) + " es el de la mitad")