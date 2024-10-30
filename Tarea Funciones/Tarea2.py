#Ingrid Vazquez 240090 Tarea 2 Numero factorial 
def factorial():
    fac=1
    n=int(input("Ingrese el numero deseado: "))
    for i in range (1,n+1) :
        fac*=i
    print(f"El resultado es: {fac}")
factorial()