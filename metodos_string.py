texto="mi texto compadre"
resultado=texto.upper()
print(resultado)

resultado1=texto[2].upper()
print(resultado1)   #SOLO EL CARACTER EN POS 2

resultado2=texto.split() #DIVIDE EN PALABRAS X ESPACIOS
print(resultado2)

resultado3=texto.split("m") #CRITERIO DE SEPARACION POR LETRA
print(resultado3)

A= "het"
B= "hemhogo"
C= "KUXHR"
D= " ".join([A,B,C]) #JOIN DE STRINGS
print(D)

resultado4=texto.find("t") #buscar y te indica la posicion
print(resultado4)

resultado5=texto.replace("mi", "tu") #1 remplazado 2 remplazante
print(resultado5)