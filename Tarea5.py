#Ingrid Vazquez 240090 Tarea 5 Horas
def convertir(minutos):
    horas=minutos//60
    min=minutos%60
    return horas,min
minutos=int(input("Ingrese los minutos a convertir"))
horas,min=convertir(minutos)
print(f"Los minutos {minutos} son {horas} Horas con {min} minutos ")
