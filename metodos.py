class Pajaro:
    alas = true

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pío, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")

piolin = Pajaro(self,"amarillo", "canario")
piolin.volar(50)
piolin.piar()