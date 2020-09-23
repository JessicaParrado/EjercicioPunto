import math
from Figura import Figura
from Punto import Punto


class Circulo(Figura):

        def __init__(self, Centro, radio):
                self.Centro = Centro
                self.radio = radio

        def areaCirculo(self):

            area = math.pi * self.radio ** 2;
            return round(area);

        def DeterminarSiHayPunto(self, p):
            return (p.hallarDistancia(self.Centro) <= self.radio)

        def hallarPerimetro(self):

            perimetro = 2 * math.pi * self.radio;
            return perimetro;
