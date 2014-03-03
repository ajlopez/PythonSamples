
import unittest
from distancias import desplaza

class DistanciasTests(unittest.TestCase):
    def test_distancia_cero(self):
        result = desplaza(0, 0, 0, 0)
        self.assertEqual(0, result.latitud)
        self.assertEqual(0, result.longitud)

    def test_distancia_112_kms_este(self):
        result = desplaza(0, 0, 0, 112)
        self.assertAlmostEqual(0, result.latitud)
        self.assertTrue(result.longitud >= 1)
        self.assertTrue(result.longitud <= 1.1)

    def test_distancia_112_kms_oeste(self):
        result = desplaza(0, 0, 180, 112)
        self.assertAlmostEqual(0, result.latitud)
        self.assertTrue(result.longitud <= -1)
        self.assertTrue(result.longitud >= -1.1)

    def test_distancia_112_kms_este_a_latitud_60(self):
        result = desplaza(60, 0, 0, 112)
        self.assertAlmostEqual(60, result.latitud)
        self.assertTrue(result.longitud >= 2)
        self.assertTrue(result.longitud <= 2.1)

    def test_distancia_112_kms_oeste_a_latitud_60(self):
        result = desplaza(60, 0, 180, 112)
        self.assertAlmostEqual(60, result.latitud)
        self.assertTrue(result.longitud <= -2)
        self.assertTrue(result.longitud >= -2.1)

    def test_distancia_112_kms_este_a_latitud_60_sur(self):
        result = desplaza(-60, 0, 0, 112)
        self.assertAlmostEqual(-60, result.latitud)
        self.assertTrue(result.longitud >= 2)
        self.assertTrue(result.longitud <= 2.1)

    def test_distancia_112_kms_oeste_a_latitud_60_sur(self):
        result = desplaza(-60, 0, 180, 112)
        self.assertAlmostEqual(-60, result.latitud)
        self.assertTrue(result.longitud <= -2)
        self.assertTrue(result.longitud >= -2.1)

    def test_distancia_112_kms_norte(self):
        result = desplaza(0, 0, 90, 112)
        self.assertTrue(result.latitud >= 1)
        self.assertTrue(result.latitud <= 1.1)
        self.assertAlmostEqual(0, result.longitud)

    def test_distancia_112_kms_sur(self):
        result = desplaza(0, 0, 270, 112)
        self.assertTrue(result.latitud <= -1)
        self.assertTrue(result.latitud >= -1.1)
        self.assertAlmostEqual(0, result.longitud)

    def test_distancia_112_kms_norte_desde_punto_10(self):
        result = desplaza(10, 10, 90, 112)
        self.assertTrue(result.latitud >= 11)
        self.assertTrue(result.latitud <= 11.1)
        self.assertAlmostEqual(10, result.longitud)

    def test_distancia_112_kms_sur_desde_punto_10(self):
        result = desplaza(10, 10, 270, 112)
        self.assertTrue(result.latitud <= 9)
        self.assertTrue(result.latitud >= 8.9)
        self.assertAlmostEqual(10, result.longitud)
        
if __name__ == '__main__':
    unittest.main()        