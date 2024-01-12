# from Modulos.ModuloOcupado import *
# from Modulos.Subpackage.Saludos import *
#
# saludar()
#
# print(suma(8, 5))
#
# saludar1("Elisa")

import unittest
import cambiatextoUnit

class ProbarCambiso(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "Buen dia"
        resultado = cambiatextoUnit.texto_title(palabra)
        self.assertEqual(resultado, "BUEN DIA")



if __name__ == "__main__":
    unittest.main()