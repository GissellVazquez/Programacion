#Ingrid Vazquez 240090 Actividad Tabla de multiplicar 
#Tabla de multiplicar: Dado un número entero x, 
# imprime la tabla de multiplicar para ese número hasta un cierto límite 
# (por ejemplo, las primeras 10 multiplicaciones). Por ejemplo, si x es 7, mostraría:
#7 × 1 = 7
#7 × 2 = 14
#7 × 10 = 70
n=int(input("Ingrese el numero de la tabla que desea: "))
if n<=10:
    for i in range (1, 11):
        r=n*i
        print(f"{n} x {i}= {r}")