from unittest import TestCase

from Punto import Punto


class Test(TestCase):
    def test_punto(self):
        punto1 = Punto(1, 0)
        punto2 = Punto(-1, 0)
        r = punto1.hallarDistancia(punto2)
        self.assertEqual(r,2)
