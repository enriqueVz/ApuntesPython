nombres = ["Ana","Hugo","Fermín"]
edades = [65,29,42]

#to xd
combinados =zip(nombres,edades)

print(combinados)
combinados1 =list(zip(nombres,edades))
print(combinados1)

for nombre, edad in combinados1:
    print(f"{nombre} tiene {edad} años.")