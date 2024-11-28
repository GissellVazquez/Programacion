import os
import time
from preguntas import materias

def mostrar_monito(intentos):
    """Función para mostrar el monito con animación en la consola."""
    monitos = [
        """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
  -----|-----
""",
        """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
  -----|-----
""",
        """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
  -----|-----
""",
        """
   -----
   |   |
   O   |
  /|   |
       |
       |
  -----|-----
""",
        """
   -----
   |   |
   O   |
   |   |
       |
       |
  -----|-----
""",
        """
   -----
   |   |
   O   |
       |
       |
       |
  -----|-----
""",
        """
   -----
   |   |
       |
       |
       |
       |
  -----|-----
"""
    ]
    print(monitos[intentos])

def seleccionar_materia():
    """Función para que el usuario seleccione la materia de las preguntas."""
    materias_lista = list(materias.keys())
    print("Selecciona una materia:")
    for i, materia in enumerate(materias_lista, 1):
        print(f"{i}. {materia.capitalize()}")
    print(f"{len(materias_lista) + 1}. Salir del juego")
    
    try:
        seleccion = int(input("Ingresa el número de la materia: ")) - 1
        if seleccion == len(materias_lista):
            print("Saliendo del juego...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        elif seleccion < 0 or seleccion >= len(materias_lista):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opción no válida. Por favor, intenta de nuevo.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return seleccionar_materia()
        return materias_lista[seleccion]
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entrada inválida. Por favor, ingresa un número.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        return seleccionar_materia()

def jugar_adivinanza():
    """Función para jugar al ahorcado."""
    vidas = 3  # Número de vidas del jugador
    materia = seleccionar_materia()
    niveles = sorted(materias[materia].keys())
    nivel_actual = 0  # Nivel inicial

    while vidas > 0 and nivel_actual < len(niveles):
        nivel = niveles[nivel_actual]
        print(f"\nNivel {nivel}\n")
        preguntas_respuestas = materias[materia][nivel]
        
        for pregunta, respuesta in preguntas_respuestas:
            palabra = respuesta.lower()  # Selecciona la respuesta de la pregunta
            letras_adivinadas = set()  # Conjunto de letras adivinadas
            intentos = 6  # Número de intentos

            while intentos > 0:
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
                mostrar_monito(intentos)  # Mostrar el monito antes de cada intento
                
                # Mostrar la pregunta, vidas y nivel antes de cada intento
                print(f"Pregunta: {pregunta}")
                print(f"Vidas: {vidas} | Nivel: {nivel}\n")
                print("Ingresa '0' para salir y regresar al menú principal.\n")
                
                # Mostrar la palabra con las letras adivinadas y el resto como "_"
                palabra_mostrada = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
                print("\n" + palabra_mostrada)
                
                # Solicitar la letra al usuario
                adivina = input("Adivina una letra: ").lower()

                # Validar la entrada del usuario
                if adivina == '0':
                    print("Saliendo y regresando al menú principal...")
                    time.sleep(2)
                    return  # Salir al menú principal
                elif len(adivina) != 1 or not adivina.isalpha():
                    print("Por favor, ingresa una sola letra.")
                    time.sleep(2)
                    continue
                elif adivina in letras_adivinadas:
                    print("Ya has adivinado esa letra. Intenta con otra.")
                    time.sleep(2)
                    continue

                # Comprobar si la letra está en la palabra
                letras_adivinadas.add(adivina)
                if adivina in palabra:
                    if all(letra in letras_adivinadas for letra in palabra):
                        print(f"¡Correcto! La palabra era '{palabra}'.")
                        time.sleep(2)
                        break
                else:
                    intentos -= 1
                    print(f"Error al adivinar, tienes {intentos} intentos restantes.")
                    time.sleep(2)
                
            if intentos == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                mostrar_monito(intentos)  # Mostrar el monito cuando se pierda
                print(f"\nPerdiste, la palabra era: {palabra}.")
                vidas -= 1  # Perder una vida
                print(f"Te quedan {vidas} vidas.")
                if vidas == 0:
                    print("Has perdido todas tus vidas. Regresando al menú principal...")
                    time.sleep(2)
                    return  # Regresar al menú principal si el jugador pierde todas las vidas
                break  # Salir del bucle de preguntas y reiniciar el nivel actual

        if vidas > 0 and intentos > 0:
            nivel_actual += 1  # Avanzar al siguiente nivel si se completan todas las preguntas del nivel actual

    if nivel_actual == len(niveles):
        print("\n¡Felicidades! Has completado todas las preguntas.")

def menu_principal():
    """Función para mostrar el menú principal."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n--- Menú Principal ---")
        print("1. Jugar al ahorcado")
        print("2. Salir del juego")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            jugar_adivinanza()
        elif opcion == "2":
            print("Saliendo del juego...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Mostrar el menú principal
menu_principal()
