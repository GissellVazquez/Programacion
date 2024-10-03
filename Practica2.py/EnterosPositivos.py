#Ingrid Vazquez 240090 Practica2 Diferencia entre 2 enteros 30/Sept/24
#Calcular la diferencia entre dos enteros positivos: Crearemos un algoritmo
#que reciba dos enteros positivos distintos y calcule la diferencia entre el número
#mayor y el menor. Además, aseguraremos que el programa siempre muestre 6
#como resultado, independientemente del orden de entrada (por ejemplo, tanto
#para 9 y 15 como para 15 y 9).
n1=int(input("Ingrese el primer numero "))
n2=int(input("Ingrese el segundo numero "))
if n1<n2:
    d=(n1-n2)*(-1)
    print(f"Su resultado es: {d}")
if (n1>n2):
    R=n1-n2
    print(f"El resultado es: {R}")
