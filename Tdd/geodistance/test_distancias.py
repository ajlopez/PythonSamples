
import unittest
from distancias import Distancias

class DistanciasTests(unittest.TestCase):
    def test_distancia_cero(self):
        result = Distancias.desplaza(0, 0, 0, 0)
        self.assertEqual(0, result.latitud)
        self.assertEqual(0, result.longitud)

if __name__ == '__main__':
    unittest.main()        