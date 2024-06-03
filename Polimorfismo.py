class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice killo tus muerto")

vaca1 = Vaca('Aurora')
oveja1 = Oveja("perrosanxe")


animales = [vaca1, oveja1]

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)