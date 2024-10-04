#Ingrid Vazquez 240090 Practica3 Categorizacion de edades
#Crear un programa que pida al usuario su edad y le indique a que grupo etario pertenece.
#Infancia (0 a 6 anos)
#Ninez (6 a 12 anos)
#Adolescencia (12 a 20 anos)
#Juventud (20 a 25 anos)
#Adultez (25 a 60 anos)
#Ancianidad (60 anos en adelante)
print(" ")
print("Categorizacion de edades ")
edad=int(input("Ingrese su edad "))
if edad <=6:
    print("Esta en la categoria de INFANCIA")
elif edad <=12:
    print("Esta en la categoria NINEZ")
elif edad <=20:
    print("Esta en la categoria ADOLESCENCIA")
elif edad <=25:
    print("Esta en la categoria JUVENTUD")
elif edad <=60:
    print("Esta en la categoria ADULTEZ")
else:
    print("Esta en la categoria ANCIANIDAD")

