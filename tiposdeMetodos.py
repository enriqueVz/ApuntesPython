class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pío")

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"ahora tu pájaro es {self.color}")

    @classmethod
    def poner_webos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(piolin.alas)

    @staticmethod
    def mirar():
        print("El pájaro mira")

piolin = Pajaro("amarillo", "canario")

piolin.poner_webos(3)