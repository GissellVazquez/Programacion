#Ingrid Vazquez 240090 Tarea2. Divisor
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla:
# a) La <n> entre <m> da un cociente <c> y un resto <r>.
# b)Donde <n> y <m> son los números introducidos por el usuario.
# c) Y <c> y <r> son el cociente y el resto de la división entera respectivamente.
print("Divisiones")
print(" ")
den= input("Ingrese el dividiendo deseado: ")
div = input("Ingrese el divisor deseado: ")
resu=str(int(den)//int(div))
residuo=str(int(den)%int(div))
print(f"El modulo de la division {den}/{div} es {resu}")
print(f"El residuo de la division {den}/{div} es {residuo}")
