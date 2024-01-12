# METODOS ESPECIALES

class Libro:

    def __init__(self, autor, titulo, cant_paginas):
        self.autor = autor
        self.titulo = titulo
        self.cant_paginas = cant_paginas

    def __str__(self):
        return f'Título: "{self.titulo}", escrito por {self.autor}'

    def __len__(self):
        return self.cant_paginas

libro1 = Libro("Stephen King", "It", 1032)


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.cantidad_canciones = canciones

    # Da un formato de como se mostraran los atributos  -toString-
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.cantidad_canciones

    def __del__(self):
        print(f"Se ha eliminado el cd {self.titulo}")

cd_mio = CD('Pink Floyd', "The Wall", 24)

# delete la instancia
del cd_mio

