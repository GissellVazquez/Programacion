#Ingrid Vazquez 240090 Practica2. Numero Mayor 30/Sept/24
#Encontrar el mayor entre tres números: Dadas tres variables enteras num1,
#num2 y num3, debemos encontrar el número más grande entre ellos y
#almacenarlo en una variable entera llamada max.
N1=int(input("Ingrese el primer numero "))
N2=int(input("Ingrese el segundo numero "))
N3=int(input("Ingrese el tercer numero "))
max= N1
if N2 >max:
    max=N2
if N3 >max:
    max=N3
print(f"Su numero mayor es {max}")