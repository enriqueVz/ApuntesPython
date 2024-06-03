miset = set([1,2,3,4,5,6])  #Solo admite un tipo de dato! Y NO PUEDE REPETIRSE EL DATO, PYTHON LO IGNORARÁ
print(type(miset))
print(miset)
miset1= {1,2,3,4,5,6} #tipos de datos que quieras
print(type(miset1))
print(len(miset1))

s1 = {1,2,3}
s1.add(4) #añadimos el elemento
s1.remove(3) #eliminamos el elemento , PUEDE USARSE DISCAR TMB
s2 = {4,5,6}
s2.pop() #elimina random
s3= s1.union(s2) #crea una sola tabla de las otras dos

#EL CLEAR ELIMINA LOS DATOS DE LA TUPLA

print(s1)
print(s2)