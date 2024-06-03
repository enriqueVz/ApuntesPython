

def letras_unicas_ordenadas(palabra):
    # Convertir la palabra en un conjunto para eliminar duplicados
    letras_unicas = set(palabra)
    # Convertir el conjunto en una lista y ordenarla
    letras_ordenadas = sorted(letras_unicas)
    # Unir la lista en una cadena y devolverla
    return ''.join(letras_ordenadas)

# Ejemplo de uso
resultado = letras_unicas_ordenadas("awitadekoko")
print(resultado)  # Salida esperada: 'abcd'
