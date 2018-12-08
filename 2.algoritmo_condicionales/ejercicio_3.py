#En un juego de preguntas a las que se responde "Si" o "No" gana quien responda correctamente tres preguntas. Si se responde mal a cualquiera de ellas ya no se pregunta la
#siguiente y termina el juego. Las preguntas son:
print("Bienvenidos al juego de quien quiere ser millonario Si/No")

print("¿Colon descubrio America?")
respuesta = str(input())
if respuesta == "Si" or respuesta == "SI": 
    print("Su respuesta es correcta!! \nsiguiente pregunta\n")

    print("Vamos a la siguiente pregunta")
    print("¿La independencia de Mexico fue en el año 1810?")
    respuesta = str(input())
    if respuesta == "Si" or respuesta == "SI":
        print("Su respuesta es correcta!! \nsiguiente pregunta\n")
    
        print("Vamos por la ultima pregunta :D")
        print("¿The Doors fue un grupo de rock americano?")
        respuesta = str(input())
        if respuesta == "Si" or respuesta == "SI":
            print("Su respuesta es correcta!! \nsiguiente pregunta\n")
            
        else: 
            print("Lo sentimos su respuesta es incorrecta :(")
    
    else:
        print("Lo sentimos su respuesta es incorrecta :(")

else:
    print("Lo sentimos su respuesta es incorrecta :(")

