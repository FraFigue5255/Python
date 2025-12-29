#Herencia: La herencia permite crear clases nuevas basadas en otras.
class Animal:
    def hablar(self):
        print("El animal hace un sonido")
class Perro(Animal):
    def hablar(self):
        print("Guau")
a = Perro()
a.hablar()