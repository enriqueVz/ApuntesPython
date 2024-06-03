from random import shuffle
#Lista inicial

palitos = ['-','--','---','----']

#mezclar
def mezclar(lista):
    shuffle(lista)
    return lista
#print(mezclar(palitos))


#pedir al user
def probarsuerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("elige un nº del 1 al 4: ")

    return int(intento)


#comprobar intento
def checkIntento(lista, intento):
    if lista[intento -1] == "-":
        print("A lavar los platos")
    else:
        print("te salvaste")

    print(f"te ha tocado {lista[intento-1]}")


palitos_mix = mezclar(palitos)
seleccion = probarsuerte()
checkIntento(palitos_mix,seleccion)