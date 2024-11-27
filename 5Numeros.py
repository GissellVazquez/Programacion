#Ingrid Vazquez 240090 Actividad 5 numeros
#Escribe un programa que solicite al usuario ingresar 5 números y los almacene
#en un arreglo. Luego, encuentra y muestra el valor máximo y mínimo del arreglo.
#puedes usar min(), max().
# Solicitar al usuario ingresar 5 números y almacenarlos en un arreglo
numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
maximo = max(numeros)
minimo = min(numeros)
print(f"El valor máximo es: {maximo}")
print(f"El valor mínimo es: {minimo}")
