import random


def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])


def probar_suerte(resmoneda, lista_numeros):
    if resmoneda == "Cara":
        return []
    else:
        return (lista_numeros)


lista_numeros = [1, 2, 3, 4, 5, 6]

resmoneda = lanzar_moneda()
reslista = probar_suerte(resmoneda, lista_numeros)

print("Resultado del lanzamiento de la moneda:", resmoneda)
print("Resultado de la lista:", reslista)