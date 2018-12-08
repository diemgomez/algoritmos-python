#El dueño de una empresa desea planificar las decisiones financieras que tomara en el año siguiente. La manera de planificarlas depende de lo siguiente:

#a. Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para que su nuevo saldo sea de $10,000. Si su capital tiene actualmente un saldo
#positivo pedirá un prestamo bancario para tener un nuevo saldo de $20,000, pero si su capital tiene actualmente un saldo superior a los $20,000 no pedirá ningun prestamo.

#b. Posteriormente repartirá su presupuesto de la siguiente manera.
#    i. $5,000 para equipo de computo
#    ii. $2,000 para mobiliario
#Y el resto la mitad será para la compra de insumos y la otra para otorgar incentivos al personal.

#c. Desplegar que cantidades se destinaran para la compra de insumos e incentivos al personal y en caso de que fuera necesario, a cuanto ascenderia la cantidad que se pediria
#al banco.
print("Cual es el valor de su capital final")
capital = float(input())

if capital < 0:
    capital_positivo = (capital)*-1
    valor_prestamo = capital_positivo + 10000 
    capital_futuro = capital + valor_prestamo
    
elif capital > 0 and capital <= 20000:
    valor_prestamo = 20000 - capital
    capital_futuro = capital + valor_prestamo
    
selif capital > 20000:
    capital_futuro = capital
    
capital_menos_equi_mat = capital_futuro - 7000
insumos = capital_menos_equi_mat / 2
incentivos = capital_menos_equi_mat / 2

if valor_prestamo > 0:
    print("Señor gerente, usted debe de hacer un prestamo por $", valor_prestamo, "pesos.")
    
else:
    print("No debe de realizar ningun prestamo")

print("Para el siguiente año, el presupuesto será designado de la siguiente forma:")
print("Incentivos: $", incentivos)
print("Insumos: $", insumos)
