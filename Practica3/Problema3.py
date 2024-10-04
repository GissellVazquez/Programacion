#Ingrid Vazquez 240090 Practica3 Calculadora
#Crear una calculadora simple que realice operaciones basicas (suma,resta,multiplicacion y division)
#de acuerdo con la eleccion del usuario. Despues le solicitara al usuario 2 numeros para realizar 
# la operacion seleccionada.
print("Calculadora")
print("1 Para Sumar ")
print("2 Para restar ")
print("3 Para multiplicar ")
print("4 Para dividir ")
op=int (input("Que operacion desea realizar: "))
if op==1:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    r=n1+n2
    print(f"La suma de {n1} + {n2} su resultado es: {r}")
elif op==2:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    r=n1-n2
    print(f"La resta de {n1} - {n2} su resultado es: {r}")

elif op==4:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    try:
        r=n1/n2
    except ZeroDivisionError: 
        print("No se puede divivir entre 0")
        exit()
    print(f"La division de {n1} / {n2} su resultado es {r:.2f}")
elif op==3:
    n1=float(input("Ingrese el primer numero "))
    n2=float(input("Ingrese el segundo numero "))
    r=n1*n2
    print(f"La multiplicaciones de {n1} * {n2} su resultado es: {r}")
else:
    print("Opcion invalida")
