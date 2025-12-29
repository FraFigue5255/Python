#Enunciado:
#Crea una clase Coche con atributo marca y un método arrancar() que imprima:
#“el coche <marca> está arrancando”.
class Coche:
    def __init__(self, marca):
        self.marca = marca
    def arrancar(self):
        print(f"El coche {self.marca} esta arrancando")
c = Coche("Toyota")
c.arrancar()