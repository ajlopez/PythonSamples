
import unittest
from distancias import desplaza

class DistanciasTests(unittest.TestCase):
    def test_distancia_cero(self):
        result = desplaza(0, 0, 0, 0)
        self.assertEqual(0, result.latitud)
        self.assertEqual(0, result.longitud)

    def test_distancia_112_kms_este(self):
        result = desplaza(0, 0, 0, 112)
        self.assertEqual(0, result.latitud)
        self.assertTrue(result.longitud >= 1)

    def test_distancia_112_kms_oeste(self):
        result = desplaza(0, 0, 180, 112)
        self.assertEqual(0, result.latitud)
        self.assertTrue(result.longitud <= -1)
        
if __name__ == '__main__':
    unittest.main()        