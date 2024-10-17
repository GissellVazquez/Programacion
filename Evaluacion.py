#Ingrid Vazquez 240090 Evaluacion 
#Realice un programa que resuelva:
#En un grupo de 15 alumnos de UPBC, se busca nombrar a un jefe de grupo madiante el voto de cada uno
#de ellos, todo esto en presencia de su maestro asesor. Se decidio una votacion los 3 candidatos son Hugo, Paco, y Luis.
#El maestro asesor les solicito que el primer lugar sea el jefe de grupo y el segundo lugar sera el tesorero 
# a) Queremos saber quien sera el jefe de grupo, con cuantos votos y porcentaje, e igual con el tesorero
# c) Al 3er lugar le daremos las gracias por participar 
contador=0
Prom=0
H=0
P=0
L=0
print("Votacion ")
print("Candidatos: 1)Hugo 2)Paco 3)Luis ")
for contador in range (1,3):
     while contador <15:
        n=int(input("Ingrese su voto "))
        if n==1:
            H=H+1
            Prom=H/15*100
        elif n==2:
            P=P+1
            Prom1=P/15*100
        elif n==3:
            L=L+1
            Prom2=L/15*100
        contador=contador+1
     else:
         print("Opcion invalida")
print(f"El candidato Luis tiene {L} Votos con un porcentaje de {Prom2:.2f}")
print(f"El candidato Paco tiene tiene {P} votos con un porcentaje de {Prom1:.2f}")
print(f"El candidato Hugo tiene {H} votos con un porcentaje de {Prom:.2f}")

    