#Ingrid Vazquez 240090 Actividad 2 Factorial 
#Factorial de un número: Dado un número entero no negativo n, calcula su factorial 
# (el producto de todos los enteros positivos desde 1 hasta n). 
# Por ejemplo, el factorial de 5 es 5! = 5 × 4 × 3 × 2 × 1.
numero=int(input("Ingrese el numero deseado: "))
fac=1
for i in range (1, numero, 1):
    fac *= i
print(f"La factorial es: {fac}")