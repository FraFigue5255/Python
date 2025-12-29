#Enunciado: Crear una clase Estudiante con:
#nombre
#lista de notas
#método promedio()
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre= nombre
        self.notas=notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)
    
e = Estudiante("Carolina", [10, 8, 9])
print(e.promedio())