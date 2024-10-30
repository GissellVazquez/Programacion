#Ingrid Vazquez 240090 Tarea kilometros 
def kilometros():
    print("Que operacion quiere hacer?")
    op=int(input("1. Para convertir a kilometros, 2.Para convertir a millas: "))

    if op ==1:
        km=float(input("Ingrese los kilometros que desee convertir: "))
        R=km/1.60934
        print(f"Los {km} km son {R:.2f} millas")
    elif op==2:
        milla=float(input("Ingrese las millas que desea convertir: "))
        r=milla/0.621371
        print(f"Las {milla} millas son {r:.2f} Kilometros")
    else:
        print("Opcion no valida")
kilometros()