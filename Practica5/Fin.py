#Ingrid Vazquez 240090 Practica2 Palabra Fin 
#Ejemplo de ciclo while con entrada del usuario, pedira y sumara los numeros mientras no ingrese la palabra fin.
total=0
while True:
    try:
        numero=input("Ingresa un numero (o escribe 'Fin' para terminar): ")
        if numero.lower()=="fin":
            break
        numero=int(numero)
        total+=numero
    except ValueError:
        print("Error: Ingrese un numero valido o escribe 'Fin' para terminarla")
        
print(f"La suma total es: {total}")