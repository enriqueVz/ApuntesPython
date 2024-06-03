lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1


for item in enumerate(lista):
    print(item)

mitupla = list(enumerate(lista))
print(mitupla)
print(mitupla[1])