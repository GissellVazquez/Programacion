#Ingrid Vazquez 240090 Practica2 Numero invertido 30/Sept/2024
#Invertir un número de tres dígitos: Elaboraremos un algoritmo para invertir un
#número almacenado en una variable A. Por ejemplo, si ingresamos 834, el
#programa debe dar como salida 438. El dato ingresado debe estar en un rango de 1 a 999.
N=int(input("Ingrese un numero "))
invertido=int(str(N)[::-1])
if N >=1 and N<=999:
    print(f"El numero invertido es {invertido}")
else:
    print("El numero ingresado deber ser dentro de estos valores 1 al 999")
