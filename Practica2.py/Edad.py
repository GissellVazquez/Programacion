#Ingrid Vazquez 240090 Practica 2. Edad 30/Sept/24
print(" ")
print("Programa que solicita la edad de un usuario y este imprimira si es o no es mayor de edad")
#Pedimos que el usuario que ingrese su edad
try:
    edad= int(input("Por favor, ingresa tu edad " ))
except ValueError:
    print("Debes ingresar un numero valido (Mayor a 0).")
    exit()
    #Verificamos si la persona es mayor de dedad 
if edad >= 18:
        print("Eres mayor de edad. !Puedes votar y conducir")
else:
        print("Eres menor de edad. Aun no puedes votar ni conducir")