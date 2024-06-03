import random


def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif 7 <= suma_dados < 10:
        return (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        return (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


dado1, dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1, dado2)
print(resultado)