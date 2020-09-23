import math
from unittest import TestCase

from Circulo import Circulo
from Punto import Punto



class Test(TestCase):

    def test_area_Circulo(self):
        punto1 = Punto(0, 0)
        circulo = Circulo(punto1, 5)
        r=circulo.areaCirculo()
        self.assertEqual(r, 79)


    def test_Perimetro(self):
        punto1 = Punto(-1, 1)
        circulo = Circulo(punto1, 1)
        self.assertEqual(circulo.hallarPerimetro(), 2*math.pi)


    def test_determinar_punto(self):
        a = Punto(-1, 0)
        b = Punto(4, 0)
        circulo = Circulo(a,4)
        r = circulo.DeterminarSiHayPunto(b)
        self.assertEqual(r, False)
