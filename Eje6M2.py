#Enunciado: Crea la clase Circulo que reciba un radio y tenga un método area().
import math
class Circulo:
    def __init__(self, radio):
        self.radio= radio
    
    def area(self):
        return math.pi * self.radio**2
c = Circulo(8)
print(c.area())