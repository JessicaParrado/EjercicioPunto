import math
from Figura import Figura
from Punto import Punto


class Triangulo(Figura):

    def __init__(self, punto1, punto2, punto3):
        self.punto1 = punto1
        self.punto2 = punto2
        self.punto3 = punto3
        self.distancia1=self.punto1.hallarDistancia(self.punto2)
        self.distancia2=self.punto2.hallarDistancia(self.punto3)
        self.distancia3=self.punto3.hallarDistancia(self.punto1)


    def conocerArea(self):

        area = ( self.distancia1 + self.distancia2  + self.distancia3 ) / 2;
        return area;

    def hallarPerimetro(self):
        perimetro = (self.distancia1 + self.distancia2 + self.distancia3);
        return perimetro;

    def TipoTriangulo(self):
        # self.hallarDistancia();

        if ((self.distancia1) == (self.distancia2) and (self.distancia1) == (self.distancia3) and (self.distancia2) == (self.distancia3)):
            respuesta = "Triángulo Equilátero";
        else:
            if ((self.distancia1 == self.distancia2 and self.distancia3 != self.distancia1 and self.distancia3 != self.distancia2) or (
                    self.distancia2 == self.distancia3 and self.distancia1 != self.distancia3 and self.distancia1 != self.distancia2) or (
                    self.distancia1 == self.distancia3 and self.distancia2 != self.distancia1 and self.distancia2 != self.distancia3)):
                respuesta = "Triángulo Isósceles";
            else:
                if ((self.distancia1) != (self.distancia2) and (self.distancia1) != (self.distancia3) and (
                        self.distancia2) != (self.distancia3)):
                    respuesta = "Triángulo Escaleno";

        return respuesta;

