#Ingrid Vazquez 240090 Atividad 3 Temperatura
#Crear un programa que registre las temperaturas de la última
#semana de una ciudad y calcule estadísticas básicas como la temperatura promedio, 
#la temperatura más alta y la temperatura más baja.
Temperatura=[]
for dia in range (1,8):
    T=float(input("Ingrese la temperatura del dia "))
    Temperatura.append(T)
p=sum(Temperatura)/len(Temperatura)
M=max(Temperatura)
m=min(Temperatura)
print(f"El promedio de las temperaturas es: {p:.2f}")
print(f"La temperatura maxima es: {M:.2f}")
print(f"La temperatura minima es: {m:.2f}")