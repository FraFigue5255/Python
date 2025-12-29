class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("Hola soy", self.nombre)

#Usamos el metodo de esta manera
p = Persona("Nuevo Horizonte")
p.saludar()