
import unittest
from distancias import desplaza

class DistanciasTests(unittest.TestCase):
    def test_distancia_cero(self):
        result = desplaza(0, 0, 0, 0)
        self.assertEqual(0, result.latitud)
        self.assertEqual(0, result.longitud)

if __name__ == '__main__':
    unittest.main()        