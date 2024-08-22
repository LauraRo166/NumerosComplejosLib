import unittest
import math
import NumerosComplejosLib

class TestNumerosComplejos(unittest.TestCase):

    def test_sumaC(self):
        self.assertEqual(NumerosComplejosLib.sumaC((1, 2), (3, 4)), (4, 6))
        self.assertEqual(NumerosComplejosLib.sumaC((15, 2), (4, 7)), (19, 9))
        
    def test_productoC(self):
        self.assertEqual(NumerosComplejosLib.productoC((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(NumerosComplejosLib.productoC((-3, -5), (7, -9)), (-66, -8))
        
    def test_restaC(self):
        self.assertEqual(NumerosComplejosLib.restaC((5, 6), (3, 4)), (2, 2))
        self.assertEqual(NumerosComplejosLib.restaC((-15, -26), (34, -42)), (-49, 16))

    def test_divisionC(self):
        self.assertAlmostEqual(NumerosComplejosLib.divisionC((4, 3), (1, -2)), (-0.4, 2.2))
        self.assertAlmostEqual(NumerosComplejosLib.divisionC((7, 5), (3, -4)), (0.04, 1.72))
        
    def test_moduloC(self):
        self.assertEqual(NumerosComplejosLib.moduloC((3, 4)), 5)
        self.assertEqual(NumerosComplejosLib.moduloC((0, 0)), 0)

    def test_conjugadoC(self):
        self.assertEqual(NumerosComplejosLib.conjugadoC((1, 2)), (1, -2))
        self.assertEqual(NumerosComplejosLib.conjugadoC((-3, -4)), (-3, 4))

    def test_faseC(self):
        self.assertAlmostEqual(NumerosComplejosLib.faseC((1, 1)), math.pi/4)
        self.assertAlmostEqual(NumerosComplejosLib.faseC((1, -1)), -math.pi/4)
        self.assertAlmostEqual(NumerosComplejosLib.faseC((-1, -1)), -3*math.pi/4)
        self.assertAlmostEqual(NumerosComplejosLib.faseC((1, -1)), -math.pi/4)

    def test_representacionPolarC(self):
        self.assertAlmostEqual(NumerosComplejosLib.representacionPolarC((3, 4)), (5, math.atan2(4, 3)))
        self.assertAlmostEqual(NumerosComplejosLib.representacionPolarC((-3, 3)), (math.sqrt(18), math.atan2(3, -3)))
    
    def test_representacionCartesianaC(self):
        esperado = (5*math.cos(math.pi/4), 5*math.sin(math.pi/4))
        self.assertAlmostEqual(NumerosComplejosLib.representacionCartesianaC((5, math.pi/4)), esperado)
        esperado = (10*math.cos(-math.pi/3), 10*math.sin(-math.pi/3))
        self.assertAlmostEqual(NumerosComplejosLib.representacionCartesianaC((10, -math.pi/3)), esperado)

        
if __name__ == '__main__':
    unittest.main()
