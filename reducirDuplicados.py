def reducir_lista(lista):
    # Eliminar duplicados convirtiendo la lista a un conjunto y de nuevo a una lista
    lista_sin_duplicados = list(set(lista))

    # Eliminar el valor más alto
    if lista_sin_duplicados:
        lista_sin_duplicados.remove(max(lista_sin_duplicados))

    return lista_sin_duplicados


def promedio(lista):
    if lista:
        return sum(lista) / len(lista)
    else:
        return 0


# Ejemplo de uso
lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

print("Lista original:", lista_numeros)
print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida:", resultado_promedio)
