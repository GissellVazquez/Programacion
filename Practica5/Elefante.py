# Ingrid Vazquez 240090 Problema2 Elefantes 
#Escribe un programa que inicie mostrando en pantalla la letra de "Un elefante se columpiaba"
#iniciando con el numero 1, despues pregunta al usuario cuantos elefantes mas se columpiaran
#y debe responder un numero mas al mostrado. 
#En caso de ingresar un numero diferente, pedirle que intente de nuevo y repetir el ciclo hasta tener 10 elefantes/
Elefante=1
print(" Un elefantes se columpiaba ")
while Elefante <10:
    try:
        n=int(input("Cuantos elefantes mas se columpiaran: "))
    except ValueError:
        print("Intente de nuevo ")
    if n==Elefante+1:
        Elefante+=1
        print(f"{Elefante} Elefantes se columpiaban")
    else:
        print("Numero equivocado. intente de nuevo")