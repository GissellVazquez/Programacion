#Ingrid Vazquez 240090 Practica2 Fruteria 30/Sept/2024
#Una fruteria ofrece las manzanas con descuento segun la siguiente tabla:
#Kg Comprados    Descuento
# 0-2                0%
# 2.01 - 5          10%
# 5.01 - 10         15%
# 10.01 - adelante  20%
# Determinar cuanto pagara una persona que compre manzanas en esa fruteria.
pr=float(input("Ingrese el precio por kilo de manzana "))
kg=float(input("Ingrese los kilos de manzana "))

if kg<=2:
    descuento=0
elif kg <=5:
    descuento=0.10
elif kg <=10:
    descuento=0.15
else:
    descuento=0.20
    
pr=kg*pr
des=pr*descuento
total=pr-des

print(f"kilos comprados es de {kg:.2f}, su pago sera de: {total:.2f}") 
print(f"Has obtenido un descuento de: {descuento:.2f}")
