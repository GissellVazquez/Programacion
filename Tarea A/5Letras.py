#Ingrid Vazquez 240090 Act. 5 Letras 
#Escribe un programa que pida al usuario ingresar 5 letras y las almacene en un
#arreglo. Luego, pide al usuario que ingrese una letra a buscar y cuenta cuántas veces aparece esta letra en el arreglo.
# Solicitar al usuario ingresar 5 letras y almacenarlas en un arreglo
letras = []
for i in range(5):
    letra = input(f"Ingrese la letra {i+1}: ")
    letras.append(letra)
buscar = input("Ingrese la letra a buscar: ")
contador = letras.count(buscar)
print(f"La letra '{buscar}' aparece {contador} veces en el arreglo.")
