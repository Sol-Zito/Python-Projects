# Ahorcado
from random import choice

lista = ["Nigeria",
         "Singapare"]


def eleccion_palabra(lista):
    palabra_elegida = choice(lista)
    return palabra_elegida


def guiones_x_palabra(palabra):
    largo_palabra = len(palabra)
    guiones_necesarios = []
    i = 0
    while i < largo_palabra:
        guiones_necesarios.append("-")
        i += 1
    return guiones_necesarios


def validacion_letra():
    abecedario = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letra = ""
    esValido = False
    while not esValido:
        letra = input("Ingrese una letra: ")
        if letra in abecedario:
            esValido = True
        else:
            pass
    else:
        return letra


def gano(letras_usuario, palabra):
    letras_sin_rep = set(palabra)
    if len(letras_sin_rep) == len(letras_usuario):
        return True
    else:
        return False


def ahorcado():
    palabra = eleccion_palabra(lista)
    vidas = 6
    intentos = 0

    letras_incorrectas = set()
    letras_correctas = set()

    palabra_guiones = guiones_x_palabra(palabra)
    gano_partida = False

    if gano_partida:
        print("Has ganado la partida")
    elif not gano_partida:
        while vidas > 0 and intentos < 6:
            print("--------------------------------")
            print(f"Letras incorrectas: {letras_incorrectas},\nVidas restantes: {vidas}")

            print(f"palabra_guiones: {palabra_guiones}")
            letra = validacion_letra()

            gano_partida = True

            if letra in palabra:
                print("La letra aparece en la palabra")
                for i, l in enumerate(palabra):
                    if l == letra:
                        palabra_guiones[i] = letra
                letras_correctas.add(letra)
            else:
                print("La letra no figura")
                letras_incorrectas.add(letra)
                vidas -= 1
                intentos += 1


        else:
            print(f"Te has quedado sin vidas, la palabra era {palabra}")




ahorcado()
