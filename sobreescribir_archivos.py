archivo = open('pyprueba.txt', 'w') # o con 'a' NO SE REEMPLAZA EL CONTENT
archivo.write('''soy un 
jamon
sin melon''')

archivo.writelines(['hola ','ompare ','perro sanxe' ])



lista = ['coco ','de ','awita' ]
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()
