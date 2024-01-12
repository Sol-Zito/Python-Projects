# REPASO
from random import randint

cliente = {'nombre': 'Federico',
           'edad': 45,
           'ocupacion': 'Instructor'
           }

pelicula = {'titulo': 'Matrix',
            'fichaTecnica': {'protagonista': 'Keanu Reeves', 'director': 'Lana y Lily Wachowski'}
            }

elementos = [cliente, pelicula, 'libros']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            e = 'Es un cliente\nNombre {nombre}, edad {edad}, ocupacion {ocupacion}'
        case {'titulo': titulo,
              'fichaTecnica': {'protagonista': protagonista, 'director': director}
              }:
            e = 'Es una pelicula \nTitulo {titulo}'
        case _:
            e = 'Debe ser un libro'

