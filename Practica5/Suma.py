#Ingrid Vazquez 240090 Problema 1 Suma de numeros 
#Realiza un programa que pida numeros mientras no se ingrese uno negativo.
#Al final,se debe mostrar la suma de los numeros ingresados 
total=0
numero=int(input("Ingresa un numero "))
while numero >0:
    total=numero*(numero+1)/2
    print(f"La suma del numero es: {total} ")
    break
else:
    print("Ingrese un numero mayor a 0")

