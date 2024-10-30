#Ingrid Vazquez 240090 Tarea  3 grados
def Grados():
    print("Que operacion quiere hacer?")
    op=int(input("1. Para convertir a Celsius, 2.Para convertir a Fahrenheit: "))

    if op ==1:
        gra=float(input("Ingrese los centigrados que desee convertir: "))
        R=gra*(9/5)+32
        print(f"Los {gra} centigrados son {R:.2f} Fahrenheit")
    elif op==2:
        gr=float(input("Ingrese los fahrenheit que desea convertir: "))
        r=(gr-32)*(5/9)
        print(f"Las {gr} fahrenheit son {r:.2f} centigrados")
    else:
        print("Opcion no valida")
Grados()