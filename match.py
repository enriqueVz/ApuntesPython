cliente = {'nombre':'Federico',
           'edad':45,
             'ocupacion':'instructor'
           }
pelicula = {'titulo':'Matrix',
            'ficha_tecnica': {'protagonista':'Kenau reeves',
                              'director':'Lana y Lilly wachowski'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("es un cliente")
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
               'director': director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("cyka baba")