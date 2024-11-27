#Ingrid Vazquez 240090 Act 6 Letras
#Escribe un programa que pida al usuario ingresar 6 números y los almacene en
#un arreglo. Luego, comprueba si el arreglo está ordenado de menor a mayor y muestra el resultado.
numeros = []
for i in range(6):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
ordenado = True
for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        ordenado = False
        break
if ordenado:
    print("El arreglo está ordenado de menor a mayor.")
else:
    print("El arreglo no está ordenado de menor a mayor.")
