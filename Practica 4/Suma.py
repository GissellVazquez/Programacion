#Ingrid Vazquez 240090 Actividad 1 Suma de un numero
#Suma de los primeros N números naturales: Dado un número entero positivo N, 
#encuentra la suma de los primeros N números naturales.
#Por ejemplo, si N es 5, la suma sería 1 + 2 + 3 + 4 + 5.
numero=int(input("Ingrese el numero deseado: "))
sum=0
for i in range (0, numero + 1):
    sum +=i
print(f"La suma es: {sum}")