import os
import time
from datetime import date
import re
from pathlib import Path
import math

ruta_directorio = "C:\\Users\\solzi\\Downloads\\ProyectoDia9\\Mi_Gran_Directorio"
today = date.today()
segundos = time.time()

arch_encontrados = []
nros_encontrados = []

def recorrer_carpetas(ruta):
     for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            abrir_archivo(carpeta, arch)

def get_five_numbers(formato):
    patron = re.search(r"\d{5}", formato)
    if patron:
        return patron[0]
    else:
        return ""

def get_three_string(formato):
    patron = re.search(r'N\D{3}', formato)
    if patron:
        return patron[0]
    else:
        return ""

def patron(texto):
    patron = re.search(r"\D{3}\d{5}", texto)
    return patron[0]


def abrir_archivo(ruta, arch):

    abriendo = Path(ruta, arch)
    texto = abriendo.read_text()
    letras = get_three_string(texto)
    numbers = get_five_numbers(texto)
    if letras and numbers:
        arch_encontrados.append(arch)
        nros_encontrados.append(f"{letras}-{numbers}")
    else:
        pass
    return arch_encontrados, nros_encontrados


def mostrar_todo(archviso, nros):
    recorrer_carpetas(ruta_directorio)
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {today.strftime("%d-%m-%Y")}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archviso:
        print(f'{a}\t{nros[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(nros)}')
    fin = time.time()
    duracion = fin - segundos
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


mostrar_todo(arch_encontrados, nros_encontrados)

