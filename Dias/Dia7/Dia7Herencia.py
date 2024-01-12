# HERENCIA

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal nacio")
    def hablar(self):
        print("Este animal emite sonido")

class Pajaro(Animal):
    # Clase Hija tiene:
    # ATRIBUTOS HEREDADOS

    # ATRIBUTOS PROPIOS
    def __init__(self,edad, color, altura_vuelo):
        # opcion 1 mas corta
        super().__init__(edad, color)

        #self.edad = edad
        #self.color = color
        self.altura_vuelo = altura_vuelo

    # METODOS HEREDADOS

    # METODOS PROPIOS
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

    # METODOS MODIFICADOS
    def hablar(self):
        print("Pio pio")

piolin = Pajaro(2, 'amarillo', 60)
piolin.nacer()

print(Pajaro.__bases__)
print(Animal.__subclasses__())

mi_animal = Animal(5, "negro")

# ----------------------------------------------------------------

class Padre:
    def hablar(self):
        print("Hola mundo")
    pass

class Madre:
    def reir(self):
        print("Ja Ja Jaa")

    def hablar(self):
        print("Como va?")

class Hijo (Padre, Madre):
    # Clase Hija tiene:
    # ATRIBUTOS HEREDADOS

    # ATRIBUTOS PROPIOS
    velocidad = 10

    # METODOS HEREDADOS
     # metodo hablar, en este caso toma el del padre, ya que es el primero del que hereda

    # METODOS PROPIOS
    def correr(self):
        print("Corre muy rapido")

    # METODOS MODIFICADOS
    def reir(self):
        print("JaJaJaa")

class Nieto(Hijo):
    pass

# ----------------------------------------------------------------

# POLIMORFISMO

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(f"{self.nombre} dice mooo ")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(f"{self.nombre} dice bee ")



vaca1 = Vaca("Aurora")
oveja1 = Oveja("Carla")

def animal_habla(animal):
    animal.hablar()


animal_habla(oveja1)