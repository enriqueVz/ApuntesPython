def devolver_distintos(a,b,c):
        suma = a + b + c
        if suma > 15:
            return max(a,b,c)
        elif suma < 10:
            return min(a,b,c)
        else:
            numeros =[a, b, c]
            numeros.sort()
            return numeros[1]


resultado1 = devolver_distintos(5, 5, 5)  # La suma es 15, debe devolver el número intermedio
resultado2 = devolver_distintos(10, 3, 2)  # La suma es 15, debe devolver el número intermedio
resultado3 = devolver_distintos(1, 1, 1)  # La suma es 3, debe devolver el menor
resultado4 = devolver_distintos(10, 10, 10)  # La suma es 30, debe devolver el mayor
print(resultado1)  # Salida esperada: 5
print(resultado2)  # Salida esperada: 3
print(resultado3)  # Salida esperada: 1
print(resultado4)  # Salida esperada: 10