# REPASANDO METODOS
from random import shuffle

palabra = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
# print(palabra.lstrip(",:%_#"))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
# print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}


# print(marcas_tv.isdisjoint(marcas_smartphones))

# ----------------------------------------------------------------
# FUNCIONES

# def nombre_nombre(): '''esta funcion se encarga de ...''' codigo

def invertir_palabra(palabra):
    valordado = palabra[::-1]
    return valordado.upper()


# print(invertir_palabra(frutas[0]))

# ----------------------------------------------------------------
def chequear(numero):
    lista1 = []
    for i in numero:
        if i in range(100, 1000):
            lista1.append(i)
        else:
            pass

    return lista1


lista = [585, 99, 110]
# print(chequear(lista))
# ----------------------------------------------------------------
precio_cafe = [('Capuccino', 1.5), ('Expresso', 1.2), ('Moka', 1.3)]


def cafe_mas_caro(listas):
    precio_mayor = 0
    cafe_caro = ''

    for cafe, precio in listas:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass
    return cafe_caro, precio_mayor


# print(cafe_mas_caro(precio_cafe))

# ----------------------------------------------------------------

# Lista inicial
palitos = ['-', '--', '---', '----', '-----']


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedir intentos
def probar_suerte():
    nro = ''
    while nro not in ['1', '2', '3', '4']:
        nro = input("Ingrese un nro del 1 al 4: ")
    return int(nro)


# Comprobar intentos
def chequear_intento(lista, intento):
    palito = lista[intento - 1]
    match palito:
        case '-':
            return "Perdiste"
        case '-----':
            return "Te salvaste"
    return f"Te toco {palito}"


# listaMezclada = mezclar(palitos)
# eleccionUsuario = probar_suerte()
# chequear_intento(listaMezclada, eleccionUsuario)

# ejercicio

from random import *


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado2, dado1


def evaluar_jugada(a, b):
    suma_dados = a + b
    mensaje = ''

    if suma_dados <= 6:
        return "La suma de tus dados es " + str(suma_dados) + ". Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return "La suma de tus dados es " + str(suma_dados) + ". Tienes buenas chances"
    elif suma_dados >= 10:
        return "La suma de tus dados es " + str(suma_dados) + ". Parece una jugada ganadora"

    return mensaje


a, b = lanzar_dados()
# print(evaluar_jugada(a, b))

# EJERCICIO

# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros),
# y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más
# alto. El orden de los elementos puede modificarse.
# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y
# que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

lista_numeros = [1, 2, 15, 7, 2]

lista_numeros.clear()


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()  # lista[::1]
    lista.pop()
    return lista


def promedio(lista_ordenada):
    suma = 0
    cantidad = len(lista_ordenada)
    for n in lista_ordenada:
        suma += n
    return suma / cantidad


# CARA CRUZ
def lanzar_moneda():
    eleccion = ["Cara", "Cruz"]
    return choice(eleccion)


# Funciones con argumentos
def suma1(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def suma(*args):
    return sum(args)


def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        cuadrado = arg ** 2
        suma += cuadrado
    return suma


def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    return suma


def persona_numeros(*args):
    nombre = ''
    suma_numeros = 0
    for indice, arg in enumerate(args):
        if indice == 0:
            nombre = arg
        else:
            suma_numeros += arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"


def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'


def cantidad_atributos(**kwargs):
    return len(kwargs)


def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista


def describir_persona(nombre, **kwargs):
    mensaje = f"Características de {nombre}:\n"
    for clave, valor in kwargs.items():
        mensaje += f"{clave}: {valor}\n"
    return mensaje


# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.


def devolver_distintos(uno, dos, tres):
    suma = sum((uno, dos, tres))
    lista = [uno, dos, tres]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido"
# debería devolver ['d','e','i','n','o','r','t']

def letras_unicas(texto):
    lista = []
    for i in texto:
        lista.append(i)
    sinDuplicado = list(set(lista))
    sinDuplicado.sort()
    return sinDuplicado


letras_unicas("entretenido")


def letras_unicas1(texto):
    mi_set = set()
    for letra in texto:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista


letras_unicas1("entretenido")


# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False


def ceros_vecinos(*args):
    for indice, nro in enumerate(args):
        if nro == 0:
            if args[indice] == args[indice + 1]:
                return True
            else:
                return False


# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(numero):
    primos = [2]
    contador = 3

    if numero < 2:
        return 0

    while contador <= numero:
        for n in range(3, contador, 2):

            if contador % n == 0:
                contador += 2
                break
        else:
            primos.append(contador)
            contador += 2

    return len(primos)

