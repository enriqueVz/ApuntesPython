mi_archivo = open('pyprueba.txt')

unalinea = mi_archivo.readline()
print(unalinea.rstrip())

unalinea = mi_archivo.readline()
print(unalinea.upper())

unalinea = mi_archivo.readline()
print(unalinea)

for l in mi_archivo:
    print("aqui dice: " + l)

todas = mi_archivo.readlines() 
mi_archivo.close()

