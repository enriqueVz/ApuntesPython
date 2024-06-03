lista = ['a','b','c']

for letra in lista:
    nºletra =lista.index(letra) + 1
    print(f"Letra {nºletra}: {letra}")

list = [ 'kike','pulido','garrido','juanma','lechu']

for nombre in list:
    if nombre.startswith("g"):
        print(nombre)
    else:
        print("yo k se primo")

nºs =[1,2,3,4,5,6]
mivalor = 0
for numero in nºs:
    mivalor = mivalor + numero
    print(mivalor)
print(mivalor)

for letra in 'python':
    print(letra)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)