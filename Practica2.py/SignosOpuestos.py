#Ingrid Vazquez 240090 Practica2 Signos opuestos 30/Sept/24
#Determinar si dos números tienen signos opuestos: Escribiremos un
#algoritmo que lea dos números enteros como entrada y muestre el mensaje
#“Signos Opuestos” solo si uno de los números es positivo y el otro es negativo.
n1 = int(input("Ingrese el primer numero "))
n2= int(input("Ingrese el segundo numero "))
if n1>0 and n2>0:
    print("Sginos iguales")
else:
    print("Signos opuestos")