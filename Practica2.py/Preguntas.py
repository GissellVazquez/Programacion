#Ingrid Vazquez 240090 Practica2 Preguntas 30/Sept/2024
#En un juego de preguntas a las que se responde si o no gana quien responda correctamente las 3 preguntas
#Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego

print("Juego de preguntas")
print(" ")

Respuesta=str(input("Colon descubrio America? " ))
if Respuesta=="Si": 
    Respuesta=str(input("La Indepencia de Mexico fue en 1810?"))
    if Respuesta=="Si":
        Respuesta=str(input("The Door es una banda de Rock Americana?"))
        if Respuesta=="Si":
            print("Felicidades has ganado")
        else:
            print("Incorrecto")