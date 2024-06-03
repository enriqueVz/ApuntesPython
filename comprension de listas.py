palabra = 'python'

lista = []
for letra in palabra:
    lista.append(letra)

print(lista)


#ma fasi killo
lista1 = [letra for letra in palabra]
print(lista1)

listanum = [n for n in range (0,100)]
print(listanum)

listanum1 = [n / 2 for n in range (0,50,2)]
print(listanum1)

listanum2= [n if n * 2 > 10 else 'no' for n in range (0,50,2)]
print(listanum2)

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)