#Ingrid Vazquez 240090 Practica3 Veterano
# En la Ponduka State University, los veteranos sólo pagan $30 (dólares)
#por asignatura mientras que los demás (regulares) pagan $50 por asignatura. Escriba
#un algoritmo en el que el usuario introduce los datos del estudiante (Vet o Reg) y el
#número de asignaturas. La salida debe indicar si el estudiante es de la categoría
#veterano o regular e indicar el número de materias y los costos de la colegiatura. 
print("PONDUKA STATE UNIVERSITY")
print("Alumno usted es", " " "1) Para veterano ", " 2) Alumno Regular")
print(" ")
usuario=int(input("Ingrese el numero correspondiente "))
if usuario==1:
    mat=int(input("Ingrese las materias reprobadas "))
    pago= 30*mat
    print(f"Alumno veterano su pago sera de {pago} dolares")
elif usuario==2:
    mat=int(input("Ingrese las materias reprobadas "))
    pago= 50*mat
    print(f"Alumno regular, su pago sera de {pago} dolares")
else:
    print("Opcion invalida. Intente de nuevo")