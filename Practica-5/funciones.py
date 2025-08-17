def saludar():
    print("¡Hola, bienvenido a Python!")

saludar()

def saludar(nombre):
    print(f"Hola {nombre}, ¿cómo estás?")

saludar("Rafael")


def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)


def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)


def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

x, y = operaciones(10, 4)
print("Suma:", x, "Resta:", y)

