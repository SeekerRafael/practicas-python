
numeros = [10, 5, 8, 20, 3]
print(min(numeros))


numeros = [10, 5, 8, 20, 3]
print(max(numeros))

letras = ["a", "x", "m", "b"]
print(min(letras))  # a
print(max(letras))  # x


edades = {"Ana": 25, "Luis": 30, "María": 22}

print(min(edades))           # Ana (min por llave)
print(max(edades))           # María (max por llave)
print(min(edades.values()))  # 22
print(max(edades.values()))  # 30
