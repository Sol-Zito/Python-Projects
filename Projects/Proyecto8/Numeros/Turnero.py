def turno_cosmetico():
    num = 1
    while True:
        yield f"C - {num}"
        num += 1


def turno_medicamentos():
    num = 1
    while True:
        yield f"F - {num}"
        num += 1


def turno_perfumeria():
    num = 1
    while True:
        yield f"P - {num}"
        num += 1


def decorador(rubro):
    return f"Su turno es:\n{rubro}\nAguarde y sera atendido."


perfu = turno_perfumeria()
med = turno_medicamentos()
cos = turno_cosmetico()


def mensaje(turno):
    rubro = ''
    if turno == '1':
        rubro = next(cos)
    elif turno == '2':
        rubro = next(perfu)
    elif turno == '3':
        rubro = next(med)
    return rubro
