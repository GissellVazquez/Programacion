#Ingrid Vazquez 240090 Actividad 3 Numeros pares 
#Programa que solicite 10 numeros al usuario, este debe imprimir como resultadoo
#cuantos de los numeros que ingreso el usuario son pares, impares y ceros
p=0
i=0
c=0
contador=0
while contador <10:
    n=int(input("Ingrese los numeros deseados "))
    if n==0:
        c=c+1
    elif n%2==0:
        p=p+1
    else:
        i=i+1
    contador+=1
print(f"Los numero impares son {i}")
print(f"Numero ceros son {c}")
print(f"Los numero pares son {p}")