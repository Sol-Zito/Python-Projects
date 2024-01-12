mi_texto = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = mi_texto[1]
segundaT = mi_texto.index("t", 5)  # --> cuenta desde el indice 5

desde3al20 = mi_texto[3:20]
desde2enAdelante = mi_texto[2:]
desde2al10saltando2 = mi_texto[2:10:2]

# print(desde3al20)
# print(desde2enAdelante)
# print(desde2al10saltando2)

saltando3en3 = mi_texto[::3]
alreverso = mi_texto[::-1]

# print(saltando3en3)
# print(alreverso)

# ------------------------------------------------------------
a = "Aprender"
b = "Python"
c = "para"
d = "Data"
e = "-".join([a, b, c, d])
# print(e)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
# opc1
facil = frase.replace("difícil", "fácil")
# print(facil.replace("mala", "buena"))

# opc2
# print(frase.replace("difícil", "fácil").replace("mala","buena"))

# ------------------------------------------------------------

# Lista -> array

verduleria = ["tomate", "lechuga", "papa", "calabaza"]

fiambres = ["queso", "jamon", "roqueford"]

eliminado = verduleria.pop(3)

# print(verduleria)
# print(eliminado)

# -------------------------------------------------------------

# Diccionario --> clave-valor

cliente = {
    "nombre": "Juan",
    "apellido": "Fuentes",
    "peso": 88,
    "talla": 1.76
}

# print(cliente["nombre"] + " " + cliente["apellido"])

diccionario = {"c1": 55, "c2": [10, 20, 30], "c3": cliente}

# print(diccionario['c1'])
# print(diccionario['c2'][1])
# print(diccionario['c3']["nombre"])

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}

# print(dic['c2'][1].upper())

cliente = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

print(cliente)

cliente["ocupacion"] = "Editora"
cliente["pais"] = "Colombia"

print(cliente)

# Tuples
# puede ser sin los ()
# y contener cualquier tipo de datos, mezclados
tupla = ('ab', 'c', 'd', 'ef', 'gh', 'i')

mi_tuple = (1, 2, 3, (4, 5, 6), 7, 8)

a, b, c, (d, p, f), g, h = mi_tuple

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# print(mi_tupla.count(2)) # ==> devuelve la cantidad de veces que aparece el nro 2


# set
# elementos unicos
# admite inmutables como tuples
mi_set = {1, 2, 3, mi_tupla}
mi_set1 = {3, 4, 5, 6, 5}

print(len(mi_set))