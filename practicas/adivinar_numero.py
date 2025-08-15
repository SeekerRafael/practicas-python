import random

numero_secreto = random.randint(1, 100)
intento = 0

while True:
    intento += 1
    numero = int(input("Adivina el número (1-100): "))
    if numero < numero_secreto:
        print("Demasiado bajo.")
    elif numero > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Correcto! Lo adivinaste en {intento} intentos.")
        break
