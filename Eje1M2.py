#Enunciado:
#Crea una clase Perro con atributos nombre y raza.
#Crea un perro y muestra sus atributos.
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
p = Perro("Lola", "Labradora")
print(p.nombre)
print(p.raza)
        