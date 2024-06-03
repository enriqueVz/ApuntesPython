if 10 > 9:
    print("es correcto")

x = True
if x:
    print("Es correcto")

if 5 == 2:
    print('Es correcto')
else:
    print('no es correcto')

mascota = "perro"
if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
elif mascota == "pez":
    print("tienes un pez")
else:
    print("No se que animal tienes")

edad = 16
calificacion = 9
if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Suspenso")
else:
     print("Eres adulto")
