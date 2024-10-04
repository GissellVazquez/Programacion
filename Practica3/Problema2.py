#Ingrid Vazquez 240090 Practica3 Triangulos 
#Crear un programa que pida al usuario los 3 lados de un triangulo y determine si es:
#Equilatero: Todos sus lados son iguales 
#Isosceles: Tiene 2 lados iguales y uno diferente 
#Escaleno: Todos sus lados y angulos son desiguales 
print("Determinar que tipo de triangulo es: ")
lado1= float(input("Ingrese la medida del primer lado "))
lado2= float(input("Ingrese la medida del segundo lado "))
lado3= float(input("Ingrese la medida del tercer lado "))
if lado1 == lado2 and lado3== lado1:
    print("Triangulo equilatero")
elif lado1 != lado2 and lado3 !=lado2 and lado3 !=lado1:
    print("Triangulo escaleno")
else:
    print("Triangulo isosceles")    