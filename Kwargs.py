def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}
prueba(15,50, *args, **kwargs)

def cantidad_atributos(**kwargs):
    argum = 0
    for n in kwargs:
        argum += 1
    return(argum)


def lista_atributos(**kwargs):
    return list(kwargs.values())

# Ejemplo de uso
atributos = lista_atributos(nombre="Juan", edad=25, ciudad="Madrid", profesion="Ingeniero")
print(atributos)  # La salida será ['Juan', 25, 'Madrid', 'Ingeniero']



def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Ejemplo de uso
describir_persona("maría", color_ojos="azules", color_pelo="rubio")
