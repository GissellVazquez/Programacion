#Ingrid Vazquez 240090 Practica3 Juego de adivinanza
numero_secreto =65
intentos=0
print("Bienvenidos al juego de adivinanza!")
print("Tienes que adivinar el numero secreto entre 1 y 100 ")
while True: #La condicion es true, lo que significa que el ciclo se ejecutara indefinidamente hasta 
# que se encuentre una instruccion break dentro del ciclo.
 try:
    guess=int(input("Ingresa tu intento: "))
    intentos+=1
    if guess==numero_secreto:
      print(f"Felicidades! Adivinaste el numero en {intentos} intentos")
      break
    elif guess <numero_secreto:
      print("El numero secreto es mayor, sigue intentando")
    else:
      print("El numero secreto es menor. Sigue intentando")
 except ValueError:
      print("Error: Ingrese un numero valido")
print("Gracias por jugar!")