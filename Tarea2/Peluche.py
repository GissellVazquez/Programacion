#Ingrid Vazquez 240090 Tarea2 Jugueteria
#Una juguetería tiene mucho éxito en dos de sus productos:payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
#calcular el peso de los payasos y muñecas que saldrán en cadapaquete a demanda. 
#Cada payaso pesa 112g y cada muñeca 75g.
# a. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso
#total del paquete que será enviado.
# b. ¿Cuánto se cobrará de envío, si la paquetería cobra 120 pesos por cada 600g?
print(" ")
p=float(input("Cuantos payasos se vendieron: "))
m=float(input("Cuantas munecas se vendieron: "))
payaso= (p*112)
muneca= (m*75)
print(f"El peso de los payasos es de: {payaso:.2f}gramos, y el de las munecas es: {muneca:.2f}gramos")
print(" ")
envio= (payaso + 599)//600*120
env = (muneca + 599)//600*120
print("El costo de envio por paquete")
print(" ")
print(f"Payaso {envio:.2f} pesos")
print(f"Muneca: {env:.2f} pesos")