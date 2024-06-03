from random import choice

palabras = ['kebab', 'kapsalon', 'navaja', 'airsoft']
letras_correctas = []
letras_incorrectas = []
intentos = 6
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    return palabra_elegida, len(set(palabra_elegida))

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta.")

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas):
    fin = False

    if letra_elegida in palabra_oculta:
        if letra_elegida not in letras_correctas:
            letras_correctas.append(letra_elegida)
    else:
        if letra_elegida not in letras_incorrectas:
            letras_incorrectas.append(letra_elegida)
            vidas -= 1

    if vidas == 0:
        fin = perder(palabra_oculta)
    elif all(letra in letras_correctas for letra in palabra_oculta):
        fin = ganar(palabra_oculta)

    return vidas, fin

def perder(palabra):
    print("¡Te has quedado sin vidas! :(")
    print("La palabra oculta era: " + palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("¡Felicidades, has ganado!")
    return True

palabra, _ = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, juego_terminado = chequear_letra(letra, palabra, intentos)
