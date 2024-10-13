#Ingrid Vazquez 240090 Actividad Pin

PIN= "1234"
int= 3
intentos = 0

while intentos < int:
    ingresado = input("Introduce el PIN: ")
    if ingresado == PIN:
        print("Login correcto")
        break
    else:
        intentos += 1
        print(f"PIN incorrecto. Intentos restantes: {int - intentos}")
    if intentos == int:
        print("Llamando al policía")

