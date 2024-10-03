#Ingrid Vazquez 240090 Practica 2. N par o impar 30/Sept/24
# Pedimos al usuario que ingrese un número
print("ingrese un numero y le dire si es par o impar")
try:
    numero = int(input("Por favor, ingresa el número: "))
except ValueError:
    print("Por favor solo ingresa numeros.")
    exit()

# Verificamos si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")