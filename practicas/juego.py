import random

numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-10): "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
