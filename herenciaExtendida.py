class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

        def piar(self):
            print("Este animal PIA")

    def hablar(self):
        print("Este animal HABLA")



class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo

       # super.__init__(edad,color) LO MISMO K ARRIBA

    def volar(self, metros):
        print(f"el pajaro vuela {metros} metros")









class Padre:
    def hablar(self):
        print("Hola")


class Hijo(Padre):
    pass


class Nieto(Hijo):
    pass

miNieto = Nieto()
miNieto.hablar()