#Ingrid Vazquez 240090 Tarea2 IMC
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y loalmacene en una variable, y muestre por pantalla la frase:
#a)Tu índice de masa corporal es <imc>, donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
print("Calcular el IMC")
kg = float(input("Ingrese su peso en kg: "))
est= float(input("Ingrese su estatura en metros: "))
imc= kg/(est*est)
print(f"Tu índice de masa corporal es {imc:.2f}")