import math

class Punto:
    def __init__(self, x, y):
         self.x = x
         self.y = y


    def hallarDistancia(self,otro):
        distancia= math.sqrt(math.pow(self.x-otro.x,2) + math.pow(self.y -otro.y ,2))
        return distancia

