class Perro:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    def ladrar(self):
        print("Lolita deja de ladrar")
p = Perro("Lolita", 5)
p.ladrar()