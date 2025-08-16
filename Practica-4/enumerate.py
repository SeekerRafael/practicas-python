frutas = ["manzana", "banana", "naranja"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


numeros = [10, 20, 30, 40]

for i, num in enumerate(numeros):
    numeros[i] = num + 5

print(numeros)

# i es la posicion y num es el valor