# Clases

class Pajaro:
    def __init__(self, color, medidas, vuela):
        self.color = color
        self.tamanio = medidas
        self.puedeVolar = vuela

    # METODOS DE INSTANCIA

    # metodo de instancia, puede acceder y modificar los atributos de la clase
    def piar(self):
        print("Pio pio")

    # Pueden acceder a otrso metodos
    def volar(self, metros):
        print(f"Volando {metros} metros")
        self.piar()


    # METODOS DE CLASE

    @classmethod
    def poner_huevo(cls, cantidad):
        print(f"Puso {cantidad}  de huevos")

    # METODOS DE ESTATICOS
    # no modifican estados de la clase, ni modificar los atributos
    @staticmethod
    def mirar():
        print("El pajaro mira")




# piolin = Pajaro("Marron", 20, True)
# piolin.volar(80)

# Se puede llamar a metodo de clase, sin la necesidad de crear una instancia
# Pero a los metodos de intancia solo al crear una

Pajaro.poner_huevo(80)
#Pajaro.piar() --> Sale error
Pajaro.mirar()

class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('Humano', True, 17)
