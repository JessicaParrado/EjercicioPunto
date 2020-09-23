import math
from unittest import TestCase

from Rectangulo import Rectangulo
from Punto import Punto

class Test(TestCase):

    def test_area(self):
        punto1 = Punto(6, 1)
        punto2 = Punto(6, -1)
        punto3 = Punto(2, 1)
        punto4 = Punto(2, -1)
        rectangulo = Rectangulo(punto1, punto2, punto3, punto4)
        r=rectangulo.areaRectangulo()
        self.assertEqual(r,8)

    def test_perimetro(self):
        punto1 = Punto(-2,1)
        punto2 = Punto(2,1)
        punto3 = Punto(-2,-1)
        punto4 = Punto(2,-1)
        rectangulo = Rectangulo(punto1, punto2, punto3, punto4)
        r=rectangulo.perimetroRec()
        self.assertEqual(r,12)