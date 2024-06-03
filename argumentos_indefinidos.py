def suma(*args):

    return sum(args)

print(suma(1,3,4,5,6,7))


def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += (n ** 2)
    return total


trye = suma_cuadrados(1, 2, 3)
print(trye)


def suma_absolutos(*args):
    todos = 0
    for n in args:
        todos += abs(n)

    return todos


amoave = suma_absolutos(2, 3, 5, -7)
print(amoave)


def numeros_persona(nombre, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n

    return (f"{nombre}, la suma de tus números es {suma_numeros}")


nombre = "kike"

eltry = numeros_persona("kike", 1, 2, 3, 3, 4, 4, 5, 6, 7)
print(eltry)