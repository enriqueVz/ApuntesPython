milista=['a','b','c']
milista2=['d','e','f']
result=milista[0]
print(result)

res1= milista + milista2
res1.append('g') #añadimos la letra al final de la lista
print(res1)
res1.pop() #así sólo borra el último elemento
print(res1)

desordlist =['c','a','b']
desordlist.sort() #Así ordenamos los elementos (arranged)
print(desordlist)

milista.reverse() #Da la vuelta
print(milista)