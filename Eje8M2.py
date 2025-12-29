#Enunciado: Crear la clase Libro con:
#título
#autor
#método info() que imprima los datos
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def info(self):
        print(f"{self.titulo} - {self.autor}")
l = Libro("Los caballeros de Zodiaco", "las 12 casas")
l.info()