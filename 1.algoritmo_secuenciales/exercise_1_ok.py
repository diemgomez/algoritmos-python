#Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto
#dinero ganara depues de un mes si el banco paga a razon de 2% mensuales.
print("Bienvenidos al Banco Zemog")
print('Por indicar al capital a invertir: ')
capital_invertir = float(input())
print('¿A cuantos meses desea tener su dinero invertido?: ')
meses = int(input())

capital_futuro = capital_invertir * (1.02)**meses

print('El capital futuro de su inversion es: ', capital_futuro, ' en los ', meses, ' meses.')