#ingrid Vazquez 240090 Actividad Invertir numeros
#Escribe un programa que pida al usuario ingresar 5 números y los almacene en
#un arreglo. Luego, invierte el orden de los elementos en el arreglo y muestra el resultado.
# Solicitar al usuario ingresar 5 números y almacenarlos en un arreglo
numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
numeros_invertidos = numeros[::-1]
print("Los números en orden invertido son:")
for numero in numeros_invertidos:
    print(numero)
