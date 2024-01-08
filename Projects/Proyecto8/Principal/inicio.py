from Projects.Proyecto8.Numeros.Turnero import *


def consultar_turno():
    eleccionUser = ''
    while eleccionUser not in ['1', '2', '3']:
        eleccionUser = input("A que área desea dirigirse:\n"
                             "[1] Cosmeticos,\n"
                             "[2] Perfumeria,\n"
                             "[3] Medicamentos: ")
    else:
        return eleccionUser


def sacar_turno():
    otroTurno = input("Desea sacar un turno: ").lower()

    if otroTurno != 'si':
        print("Adios")
    else:
        inicio()


def inicio():
    turno = consultar_turno()
    tipo = mensaje(turno)
    print(decorador(tipo))
    sacar_turno()


inicio()
