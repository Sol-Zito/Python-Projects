import datetime
# from datetime import datetime

# mi_hora = datetime.time(17, 35, 51, 45)
# # se le pasan valores numerico los cuales los muestra en formato hora
# mi_dia = datetime.date(2025, 10, 17)
# # se le pasan valores numerico los cuales los muestra en formato fecha yyyy/mm/dd
# print(mi_dia.ctime())
# print(mi_dia.today())
# print(mi_hora)

# dia_hora = datetime(2025, 1, 21, 19, 00)
# print(dia_hora)

# nacimiento = datetime(1995, 3, 3)
# muerte = datetime(2040, 3, 3)
#
# vida = muerte - nacimiento
# print(f"vivio {vida.days / 360} ")

# funciones

import time
import timeit

mi_for = '''def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista'''

declaracion = '''prueba_for(10)'''

mi_while = '''def prueba_while(numero):
    lista = []
    contador = 1
    while numero >= contador:
        lista.append(contador)
        contador += 1
    return lista'''

declaracion_w = '''prueba_while(10)'''

# inicio = time.time()
# declaracion = '''prueba_for(10)'''
#
# final = time.time()
#
# print(final-inicio)
# print("--------------------------------")
# inicio_w = time.time()
# prueba_while(150000)
# final_w = time.time()
#
# print(final_w - inicio_w)

duracion_w = timeit.timeit(declaracion_w, mi_while, number=10)
print(duracion_w)

duracion = timeit.timeit(declaracion, mi_for, number=10)
print(duracion)
