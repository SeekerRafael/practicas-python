import random



#  número entero aleatorio entre 1 y 10
num = random.randint(1, 10)
print(f"randint: {num}")

# 2número decimal aleatorio entre 0 y 1
decimal = random.random()
print(f"random: {decimal}")

# elegir un elemento al azar de una lista
colores = ["rojo", "verde", "azul"]
color = random.choice(colores)
print(f"choice: {color}")

#  mezclar los elementos de una lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"shuffle: {numeros}")

# sublista aleatoria sin repetir
sublista = random.sample(numeros, 3)
print(f"sample: {sublista}")


# Número decimal aleatorio entre 1.5 y 5.5
num = random.uniform(1.5, 5.5)
print(num)