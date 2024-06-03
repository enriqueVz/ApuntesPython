monedas = 5
respuesta = 's'
while monedas > 0 and respuesta == 's':
    print(f"Tengo {monedas} monedas")
    #monedas = monedas - 1
    monedas -= 1
    respuesta = input("Quieres seguir? (s/n) ")
else:
    print("no tengo cash")

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'e':
        break
    if letra == 'o':
        continue
    print(letra)