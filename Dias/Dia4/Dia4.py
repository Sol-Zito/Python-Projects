# IF ELSE ELIF ELSE

# num1 = 0  # int(input("Ingresa un número:"))
# num2 = 0  # int(input("Ingresa otro número:"))
#
# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print(f"{num1} y {num2} son iguales")
# print("----------------------------------------------------------------")

# LOOP FOR

nombres = ["Juan", "Ignacio", "Federico", "Emma", "Julia"]
# for nombre in nombres:
#     # nomIndex = nombres.index(nombre)
#     # print(f"{nombre}, {nomIndex}")
#     if nombre.startswith("J"):
#         print(f"{nombre}")
# print("----------------------------------------------------------------")
#
# lista = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}
# var = 0
#
# for el in lista.items():
#     print(f"{el}")  # muesta clave/valor
# print("----------------------------------------------------------------")
# for el in lista.keys():
#     print(f"{el}")  # muesta clave
# print("----------------------------------------------------------------")
# for el in lista.values():
#     print(f"{el}")  # muesta valor
# nombre = "Federico"
# for el in nombre:
#     if el == "e":
#         continue # salta la letra e
#     if el == "r":
#         break # al llegar a la letra r corta
#     print(el)

# WHILE

# valorWhile = 8
# while valorWhile > 0:
# print(valorWhile)
# valorWhile -= 1
# pass --> salta esto hasta que le de un valor
# else:
# print("Cierre de ciclo")


# RANGE

# for el in range(5):
#     # va desde el 0 al 4
#     print(el)
# print("----------------------------------------------------------------")
# for el in range(5, 11):
#     # va del 5 al 10
#     print(el)
# print("----------------------------------------------------------------")
# for el in range(5, 11, 2):
#     # va del 5 al 10 saltando 2
#     print(el)
#
# lista = list(range(1,101,10))
# print(lista)

# ENUMERATE
# convierte en taples dado que es clavo/valor y clave es unica, ya que toma los indices
# for indice,elemento in enumerate(range(1, 16)):
#     print(indice, elemento)
#
# vocales = ["a", "b", "c", "d", "e", "f"]
# mi_lista = list(enumerate(vocales))
# print(mi_lista)
#
# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#
# for indice, nombre in enumerate(lista_nombres):
#     if nombre.startswith("M"):
#         print(indice)
#
# # ZIP
# # une listas
#
# nombre = ["Ana", "Jorge", "Luis", "Ana"]
# edades = [66, 56, 89, 66]
# ciudades = ["Lima", "Madrid", "Buenos Aires", "San Francisco"]
# combinados = list(zip(nombre, edades, ciudades))
# for nombre, edad, ciudad in combinados:
#     print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# # MAX & MIN
# diccionario_edades = {"Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24, "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49}
# edad_minima = min(diccionario_edades.values())
# ultimo_nombre = max(diccionario_edades.keys())


# LIBRERIA RANDOM
from random import *

aleatorio = randint(3, 88)
print(aleatorio)

decimal = uniform(1, 5)
#print(decimal)

fraccionDeEnteto = round(random())
#print(fraccionDeEnteto)

colores = [ "azul", "rojo", "verde", "amarillo"]
randomColor = choice(colores)
#print(randomColor)

shuffle(colores) # los muestra con un orden random
#print(colores)

# COMPRENSION DE LISTAS

Python = "Python"
listaNueva = [ff for ff in Python]

listanumerica = [n for n in range(0, 22, 2)]
listanumerica1 = [n for n in range(0, 22) if n % 5 == 0]
listanumerica2 = [n if n % 5 == 0 else 'no' for n in range(0, 21)]

pies = [10, 20, 30, 40, 50]
metros = [p / 3.281 for p in pies]
#print(metros)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]

#print(grados_celsius)


# MATCH
serie = 'N022'
match serie:
    case 'N021':
        print("Serie es N021")
    case 'N022':
        print("Serie es N022")
    case 'N023':
        print("Serie es N023")
    case 'N024':
        print("Serie es N024")
    case _:
        print("No se encontro serie")
