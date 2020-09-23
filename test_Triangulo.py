import math
from unittest import TestCase

from Triangulo import Triangulo
from Punto import Punto

class Test(TestCase):

    def test_area(self):
        punto1 = Punto(4, 3)
        punto2 = Punto(2, 0)
        punto3 = Punto(6, 0)
        triangulo = Triangulo(punto1, punto2, punto3)
        r=triangulo.conocerArea()
        self.assertEqual(r, 5.60555127546399)

    def test_perimetro(self):
        punto1 = Punto(4, 3)
        punto2 = Punto(2, 0)
        punto3 = Punto(6, 0)
        triangulo = Triangulo(punto1, punto2, punto3)
        r=triangulo.hallarPerimetro()
        self.assertEqual(r, 11.21110255092798)

    def test_tipo1(self):
        punto1 = Punto(4, 3)
        punto2 = Punto(2, 0)
        punto3 = Punto(6, 0)
        triangulo = Triangulo(punto1, punto2, punto3)
        r=triangulo.TipoTriangulo()
        self.assertEqual(r,"Triángulo Isósceles")

    def test_tipo2(self):
        punto1 = Punto(0, 3)
        punto2 = Punto(-1, 0)
        punto3 = Punto(5, 0)
        triangulo = Triangulo(punto1, punto2, punto3)
        r=triangulo.TipoTriangulo()
        self.assertEqual(r,"Triángulo Escaleno")

