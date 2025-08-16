nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 22,49]


combinados = zip(nombres, edades)
print(combinados)

combinados1 = list(zip(nombres, edades))
print(combinados1)

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")


