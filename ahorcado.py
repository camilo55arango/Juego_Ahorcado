import random

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'computadora', 'teclado', 'monitor', 'raton', 'software', 'hardware']

# Función para elegir una palabra al azar
def elegir_palabra():
    return random.choice(palabras)

# Función para mostrar la palabra oculta
def mostrar_palabra_oculta(palabra, letras_adivinadas):
    oculto = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            oculto += letra
        else:
            oculto += '-'
    return oculto

# Función para pedir al usuario una letra
def pedir_letra():
    letra = input("Ingresa una letra: ")
    while not letra.isalpha():
        letra = input("Ingresa una letra válida: ")
    return letra.lower()

# Función principal del juego
def jugar_ahorcado():
    print("¡Bienvenido al juego del ahorcado!")
    palabra = elegir_palabra()
    letras_adivinadas = []
    vidas = 6

    while True:
        print("\nVidas restantes:", vidas)
        print(mostrar_palabra_oculta(palabra, letras_adivinadas))
        letra = pedir_letra()

        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            vidas -= 1
            print("Incorrecto.")

        if vidas == 0:
            print("\n¡Perdiste! La palabra era:", palabra)
            break

        if '-' not in mostrar_palabra_oculta(palabra, letras_adivinadas):
            print("\n¡Felicidades! Adivinaste la palabra:", palabra)
            break

# Ejecutar el juego
jugar_ahorcado()
