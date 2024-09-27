#Ingrid Vazquez 240090 Tarea2 Trabajo 
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# a) Después debe mostrar por pantalla la paga que le corresponde.
name= str(input("Ingrese su nombre: "))
sal= float(input("Ingrese su salario por hora: "))
hora= float(input("Ingrese las horas trabajadas "))
pago= sal*hora
print(f"Al empleado {name}, su pago es de: {pago:.2f}")