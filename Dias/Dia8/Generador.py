def mi_fucnion():
    lista = []

    for x in range(1, 5):
        lista.append(x*10)

    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# ----------------------------------------------------------------
def mi_generado1():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


gg1 = mi_generado1()
print(next(gg1))
print(next(gg1))
print(next(gg1))