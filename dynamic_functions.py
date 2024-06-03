def check_3_cifras(numero):
    return  numero in range(100,1000)

suma = 500 + 400
resultado = check_3_cifras(suma)
print(resultado)


def check_3_cifrasS(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False


 #da none porq no hay
resultaduo = check_3_cifrasS([55,99,600])
print(resultaduo)


def check_3_cifrasSs(listaa):

    listanum = []

    for n in listaa:
        if n in range(100,1000):
           listanum.append(n)
        else:
            pass



 #da none porq no hay
resultaduuo = check_3_cifrasSs([55,99,600])
print(resultaduuo)