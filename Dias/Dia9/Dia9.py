from collections import Counter, defaultdict, namedtuple, deque

# serie = Counter([2, 2, 3, 2, 1, 5, 2, 7, 2, 9, 1, 1])
#
# print(list(serie))
# print(serie.most_common())  # muestra en forma de tupla el nro y la cantidad de veces que aparece
#
# mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
#
# print(mi_dic['dos'])
#
# print('--------------------------------')
#
# dic = defaultdict(lambda: 'nada')
#
# dic['uno'] = "verde"
#
# print(dic['dos'])
# print(dic)
#
# print('--------------------------------')
#
# mi_tuple = (500, 18, 21)
#
# print(mi_tuple[1])
#
# Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
#
# Ariel = Persona("Ariel", 1.76, 79)
#
# print(Ariel[1])
# print(Ariel[2])

print("----------------")

lista = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# for i in lista:
#     lista_ciudades.appendleft(i)

print("lista_ciudades", lista_ciudades)
