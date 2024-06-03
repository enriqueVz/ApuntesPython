diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

resultado=diccionario['c1']
print(resultado)

cliente={'nombre':'juan', 'apellido':'rodriguez', 'talla':'XL'}
consulta=(cliente['talla'])
print(consulta)

cons1 = {'x1':['10','20','30']}
print(cons1['x1'][1].upper()) #sacar elementos de un dicc dentro de otro dicc, se le pueden meter los métodos de todos los strings.

print(cliente.keys()) #print de la enumeracion
print(cliente.values()) #print de los datos del dicc