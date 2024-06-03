from  random import randint
intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un nº entre el 1 y el 100. \n Tienes ocho(8) intentos para acertarlo.")

while intentos < 8:
    estimado = int(input("Cuál es el nº?"))
    intentos += 1
    if estimado not in range(1,101):
        print("tu nº no esta en el rango, jefe")
    elif estimado < numero_secreto:
        print("Mi nº es mas alto")

    elif estimado > numero_secreto:
        print("Mi nº es mas bajo")

    else:
        print(f"Felicidades {nombre}!! lo has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"lo siento, la has cagao macho. El nº secreto era {numero_secreto}!.")
