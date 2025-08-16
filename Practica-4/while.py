respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir? ')



contador = 1
while contador <= 5:
    print(contador)
    contador += 1


numero = -1
while numero < 0:
    numero = int(input("Ingresa un número positivo: "))
    if numero < 0:
        print("Ese número no es válido, intenta de nuevo")

