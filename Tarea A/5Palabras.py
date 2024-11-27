#Ingrid Vazquez 240090 Actividad Vectores
#Escribe un programa que pida al usuario ingresar 5 palabras y las almacene en
#un arreglo. Luego, ordena el arreglo alfabéticamente y muestra el resultado.
#Puedes utilizar sort().
def ingresar_palabras():
    palabras = []
    for i in range(5):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        palabras.append(palabra)
    return palabras

def ordenar_palabras(palabras):
    palabras.sort()
    return palabras

def mostrar_palabras(palabras):
    print("Las palabras ordenadas alfabéticamente son:")
    for palabra in palabras:
        print(palabra)

palabras = ingresar_palabras()
palabras_ordenadas = ordenar_palabras(palabras)
mostrar_palabras(palabras_ordenadas)
