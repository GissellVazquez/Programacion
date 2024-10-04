#Ingrid Vazquez 240090 Practica3 Vocal
#Suponiendo que se ingresa una vocal por teclado, realice un algoritmo
#para determinar si es abierta o cerrada.
voc=str(input("Ingrese una vocal ").lower())
if voc =="a" or voc== "e" or voc=="i":
      print(f"La vocal {voc} es abierta ")
elif voc =="o" or voc=="u":
       print(f"La vocal {voc} es cerrada ")
else:
      print("Ingrese una vocal: A-E-I-O-U")