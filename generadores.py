def mi_generador():
     yield 4


def mi_generador1():
    for x in range(1,5):
        yield x * 10




print(mi_generador())
g = mi_generador1()
print(next(g))
print(next(g))
print(next(g))
print(next(g)) 
