from Figura import Figura

class Rectangulo(Figura):

    def __init__(self, punto1, punto2, punto3, punto4):
        self.punto1 = punto1
        self.punto2 = punto2
        self.punto3 = punto3
        self.punto4 = punto4
        self.distancia1=self.punto1.hallarDistancia(self.punto2)
        self.distancia2=self.punto2.hallarDistancia(self.punto4)
        self.distancia3=self.punto4.hallarDistancia(self.punto3)
        self.distancia4 = self.punto3.hallarDistancia(self.punto1)

    def areaRectangulo(self):

        self.mayor=0;

        self.menor = 0;

        if (self.distancia1 >= self.distancia2 and self.distancia1 >= self.distancia3 and self.distancia1 >= self.distancia4):
            self.mayor=self.distancia1;
        else:
            if (self.distancia2 >= self.distancia1 and self.distancia2 >= self.distancia3 and self.distancia2 >= self.distancia4):
                self.mayor=self.distancia2;
            else:
                if (self.distancia3 >= self.distancia1 and self.distancia3 >= self.distancia2 and self.distancia3 >= self.distancia4):
                    self.mayor=self.distancia3;
                else :
                    if (self.distancia4 >= self.distancia1 and self.distancia4 >= self.distancia2 and self.distancia4 >= self.distancia3):
                        self.mayor=self.distancia4;


        if (self.distancia1 <=self.distancia2 and self.distancia1 <= self.distancia3 and self.distancia1 <= self.distancia4):
            self.menor=self.distancia1;
        else:
            if (self.distancia2 <= self.distancia1 and self.distancia2 <= self.distancia3 and self.distancia2 <= self.distancia4):
                self.menor=self.distancia2;
            else:
                if (self.distancia3 <= self.distancia1 and self.distancia3 <= self.distancia2 and self.distancia3 <= self.distancia4):
                    self.menor=self.distancia3;
                else :
                    if (self.distancia4 <= self.distancia1 and self.distancia4 <= self.distancia2 and self.distancia4 <= self.distancia3):
                        self.menor=self.distancia4;
        area = self.mayor * self.menor;
        return area;

    def perimetroRec(self):
        perimetro = self.distancia1 + self.distancia2 + self.distancia3 + self.distancia4;
        return perimetro;