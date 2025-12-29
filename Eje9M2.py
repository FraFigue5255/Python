#Enunciado: Crea la clase Rectangulo con métodos:
#area()
#perimetro()
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
r = Rectangulo(4, 6)
print("El area es:" , r.area(), " El perimetro es: " , r.perimetro()) 