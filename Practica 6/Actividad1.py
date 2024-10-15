#Ingrid Vazquez 240090 Actividad1 Tablas de multiplicar 
#Programa que realice las tablas de multiplicar del 1 al 3 e imprima un mensaje parecido.
for t in range (1,4):
    print(" ")
    print(f"Tabla de multiplicar {t}")
    for i in range (1, 11,):
         r=t*i
         if r%2==0:
             print(f"{t} x {i}= {r}")
         