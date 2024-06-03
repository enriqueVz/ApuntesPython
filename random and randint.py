from random import *

#cuidao con importar cosas y que la clase tenga el mismo nombre pq se jode

aleatorio = randint(1,50)
print(aleatorio)

#solo con un decimal
aleatorio1 = round(uniform(1,5),1)
print(aleatorio1)

aleatorio2 = uniform(1,5)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

colores = ["azul","rojo","amarillo","negro"]
aleatorio4 = choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))
print(numeros)

numeros2 = list(range(5,50,5))
shuffle(numeros2)
print(numeros2)