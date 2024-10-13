#Ingrid Vazquez 240090 Actividad Contador de numeros 


p = 0
n= 0
c= 0
contador = 0
while contador < 10:
    numero = int(input("Introduce un número: "))
    if numero > 0:
        p += 1
    elif numero < 0:
        n += 1
    else:
        c += 1
    contador += 1
print(f"Positivos: {p}")
print(f"Negativos: {n}")
print(f"Ceros: {c}")
